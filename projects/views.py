from django.contrib.auth import get_user_model
from django.db import models
from rest_framework import viewsets, permissions,filters
from .models import Project, ProjectMember, ProjectFile
from .serializers import ProjectSerializer, ProjectMemberSerializer, ProjectFileSerializer
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrAdmin
from django.db.models import Q
from rest_framework import status

User = get_user_model()
# 自定义权限：只允许项目创建者或管理员删除或修改项目
class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or request.user.is_admin

# 项目视图集

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]
    parser_classes = [MultiPartParser, FormParser]

    def perform_create(self, serializer):
        # 创建项目并保存项目描述图片
        image = self.request.data.get('image')
        serializer.save(created_by=self.request.user, image=image)

    def perform_update(self, serializer):
        # 更新项目时也可以更新项目描述图片
        image = self.request.data.get('image')
        serializer.save(image=image)

    @action(detail=True, methods=['GET'])
    def get_project_image(self, request, pk=None):
        # 获取项目描述图片的 URL
        project = self.get_object()
        if project.image:
            return Response({'image_url': project.image.url}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No image found for this project.'}, status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        # 返回用户创建的项目或该用户作为成员参与的项目
        user = self.request.user
        return Project.objects.filter(models.Q(created_by=user) | models.Q(members__user=user)).distinct()



# 项目成员视图集
class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # 返回当前用户参与的项目成员信息
        user = self.request.user
        return ProjectMember.objects.filter(user=user)

# 项目文件视图集
class ProjectFileViewSet(viewsets.ModelViewSet):
    queryset = ProjectFile.objects.all()
    serializer_class = ProjectFileSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # 获取项目并确保路径使用 project_id
        project = get_object_or_404(Project, pk=self.request.data.get('project'))  # 获取项目
        file_name = self.request.data.get('file_name')
        existing_file = ProjectFile.objects.filter(project=project, file_name=file_name).first()

        if existing_file:
            # 删除现有文件，允许覆盖
            existing_file.file.delete(save=False)
            existing_file.delete()

        # 保存文件时使用 project_id 生成文件路径
        serializer.save(uploaded_by=self.request.user, project=project)

    def get_queryset(self):
        # 返回当前用户参与的项目相关的文件
        user = self.request.user
        return ProjectFile.objects.filter(project__members__user=user)

    def destroy(self, request, *args, **kwargs):
        # 删除文件时，只有文件上传者或管理员有权限
        file = self.get_object()
        if file.uploaded_by == request.user or request.user.is_admin:
            return super().destroy(request, *args, **kwargs)
        else:
            return Response({'error': 'You do not have permission to delete this file.'}, status=403)


class ProjectSearchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['project_name', 'description', 'field']  # 添加对 field 的支持

    def list(self, request, *args, **kwargs):
        # 获取查询参数中的搜索关键字
        search_query = request.query_params.get('search', None)
        if search_query:
            keywords = [keyword.strip() for keyword in search_query.split(',') if keyword.strip()]
            filter_query = None

            # 构建查询条件
            for keyword in keywords:
                if filter_query is None:
                    filter_query = self.get_queryset().filter(
                        project_name__icontains=keyword
                    ) | self.get_queryset().filter(
                        description__icontains=keyword
                    ) | self.get_queryset().filter(
                        field__icontains=keyword  # 添加对 field 的搜索
                    )
                else:
                    filter_query |= self.get_queryset().filter(
                        project_name__icontains=keyword
                    ) | self.get_queryset().filter(
                        description__icontains=keyword
                    ) | self.get_queryset().filter(
                        field__icontains=keyword  # 添加对 field 的搜索
                    )

            self.queryset = filter_query

        return super().list(request, *args, **kwargs)


@api_view(['GET'])
def recommend_students(request, project_id):
    # 获取项目
    project = get_object_or_404(Project, project_id=project_id)
    project_field = project.field
    project_description = project.description
    project_name = project.project_name

    # 获取所有用户
    users = User.objects.filter(is_teacher=False)

    # 存储推荐的学生
    recommended_students = []

    for user in users:
        user_major = user.major
        user_interests = user.interests.replace('，', ',').split(',')  # 假设兴趣以逗号分隔
        print(f"Project Field: {project_field}, User Major: {user_major}, User Interests: {user_interests}")

        # 进行关键词匹配
        if (user_major.lower() in project_field.lower() or
                any(interest.lower() in project_field.lower() for interest in user_interests) or
                any(interest.lower() in project_description.lower() for interest in user_interests) or
                project_name.lower() in [interest.lower() for interest in user_interests]):
            recommended_students.append({
                'name': user.name,
                'email': user.email,
                'student_id': user.student_id,
                'school': user.school,
                'major': user.major,
                'phone': user.phone,
                'interests': user.interests,
            })

    return Response(recommended_students, status=status.HTTP_200_OK)

@api_view(['GET'])
def recommend_teachers(request, project_id):
    # 获取项目
    project = get_object_or_404(Project, project_id=project_id)
    project_field = project.field
    project_description = project.description
    project_name = project.project_name

    # 获取所有用户
    users = User.objects.filter(is_teacher=True)  # 只筛选老师

    # 存储推荐的老师
    recommended_teachers = []

    for user in users:
        user_major = user.major
        user_interests = user.interests.split(',')

        # 进行关键词匹配
        if (user_major.lower() in project_field.lower() or
                any(interest.lower() in project_field.lower() for interest in user_interests) or
                any(interest.lower() in project_description.lower() for interest in user_interests) or
                project_name.lower() in [interest.lower() for interest in user_interests]):
            recommended_teachers.append({
                'name': user.name,
                'email': user.email,
                'student_id': user.student_id,
                'school': user.school,
                'major': user.major,
                'phone': user.phone,
                'interests': user.interests,
            })

    return Response(recommended_teachers, status=status.HTTP_200_OK)