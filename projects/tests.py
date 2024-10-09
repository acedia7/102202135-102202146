import json

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Project, ProjectMember, ProjectFile
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient  # 导入 APIClient

User = get_user_model()

class ProjectTests(TestCase):

    def setUp(self):
        self.client = APIClient()  # 使用 APIClient 初始化
        self.user = User.objects.create_user(
            student_id='T123456789',
            name='Test User',
            school='Fuzhou University',
            email='testuser@fzu.edu.com',
            password='testpassword',
        )
        self.user.is_active = True
        self.user.save()

        self.token, created = Token.objects.get_or_create(user=self.user)

        self.project_data = {
            'project_name': 'Test Project',
            'description': 'A project for testing',
            'field': 'Computer Science',
            'license': 'GPL',
            'status': 'preparing',
            'is_private': False,
        }
        self.project_url = reverse('project-list')  # 假设项目视图的 URL 名称为 'project-list'
        self.project_detail_url = None

        # 使用 token 登录
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # 用户登录
        self.client.login(email='testuser@fzu.edu.com', password='testpassword')

    def test_create_project(self):
        # 测试创建项目
        response = self.client.post(self.project_url, json.dumps(self.project_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)  # 确保返回201状态
        self.assertTrue(Project.objects.filter(project_name=self.project_data['project_name']).exists())  # 确保项目被创建

    def test_get_project_list(self):
        # 测试获取项目列表
        self.client.post(self.project_url, json.dumps(self.project_data), content_type='application/json')  # 创建项目
        response = self.client.get(self.project_url)
        self.assertEqual(response.status_code, 200)  # 确保返回200状态
        self.assertContains(response, self.project_data['project_name'])  # 确保项目在列表中

    def test_update_project(self):
        # 测试更新项目
        project = Project.objects.create(**self.project_data, created_by=self.user)
        self.project_detail_url = reverse('project-detail', kwargs={'pk': project.project_id})  # 获取项目详情的 URL

        updated_data = {
            'project_name': 'Updated Project Name',
            'description': 'Updated description',
            'field': 'Data Science',
            'license': 'MIT',
            'status': 'ongoing',
            'is_private': True,
        }
        response = self.client.put(self.project_detail_url, json.dumps(updated_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)  # 确保返回200状态
        project.refresh_from_db()  # 从数据库中重新加载项目
        self.assertEqual(project.project_name, updated_data['project_name'])  # 确保项目名称已更新

    def test_delete_project(self):
        # 测试删除项目
        project = Project.objects.create(**self.project_data, created_by=self.user)
        self.project_detail_url = reverse('project-detail', kwargs={'pk': project.project_id})

        response = self.client.delete(self.project_detail_url)
        self.assertEqual(response.status_code, 204)  # 确保返回204状态
        self.assertFalse(Project.objects.filter(project_id=project.project_id).exists())  # 确保项目已被删除

    def test_file_upload(self):
        # 测试文件上传
        project = Project.objects.create(**self.project_data, created_by=self.user)
        self.project_detail_url = reverse('project-detail', kwargs={'pk': project.project_id})

        with open('test_file.txt', 'w') as f:
            f.write('This is a test file.')

        with open('test_file.txt', 'rb') as f:
            response = self.client.post(
                reverse('file-list'),  # 假设文件视图的 URL 名称为 'file-list'
                {
                    'project': project.project_id,
                    'file_name': 'test_file.txt',
                    'file': f,
                },
                format='multipart'
            )
        self.assertEqual(response.status_code, 201)  # 确保返回201状态
        self.assertTrue(ProjectFile.objects.filter(file_name='test_file.txt').exists())  # 确保文件被上传


