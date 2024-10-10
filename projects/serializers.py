from rest_framework import serializers
from .models import Project, ProjectMember, ProjectFile
from users.models import User

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ['project_id', 'created_by', 'created_at', 'updated_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        # 确保图片 URL 使用 https
        if 'image' in representation and representation['image']:
            representation['image'] = representation['image'].replace('http://', 'https://')

        return representation

class ProjectMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectMember
        fields = '__all__'
        read_only_fields = ['id']

class ProjectFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = '__all__'
        read_only_fields = ['file_id', 'uploaded_by', 'uploaded_at']
