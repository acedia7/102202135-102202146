import os
from django.db import models
from django.conf import settings

class Project(models.Model):
    LICENSE_CHOICES = [
        ('GPL', 'GPL'),
        ('MIT', 'MIT'),
        ('MPL', 'MPL'),
        ('BSD', 'BSD'),
        ('Apache', 'Apache'),
    ]

    STATUS_CHOICES = [
        ('preparing', '筹备中'),
        ('ongoing', '进行中'),
        ('completed', '已完结'),
    ]

    PRIVACY_CHOICES = [
        (True, '私密'),
        (False, '公开'),
    ]

    project_id = models.AutoField(primary_key=True)  # 自动生成唯一ID
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    field = models.CharField(max_length=255)
    license = models.CharField(max_length=10, choices=LICENSE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing')
    is_private = models.BooleanField(choices=PRIVACY_CHOICES, default=False)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image = models.ImageField(upload_to='', blank=True, null=True)

    def get_image_upload_path(self, filename="项目图"):
        """
        根据项目ID创建动态文件夹并存储项目描述图片，名称固定为‘项目图’
        """
        project_id_str = str(self.project_id)  # 获取项目ID
        # 图片路径为：project_images/<project_id>/项目图
        return os.path.join('project_images', project_id_str, filename)

    def save(self, *args, **kwargs):
        if self.image:
            self.image.name = self.get_image_upload_path()  # 使用项目ID作为路径
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name


class ProjectMember(models.Model):
    ROLE_CHOICES = [
        ('member', '成员'),
        ('admin', '管理员'),
    ]

    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='project_memberships')

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='member')

    class Meta:
        unique_together = ('project', 'user')

    def __str__(self):
        return f"{self.user.email} in {self.project.project_name}"

class ProjectFile(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='uploaded_files')
    file_name = models.CharField(max_length=255)
    file = models.FileField(upload_to='')  # 这里留空，稍后设置
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_upload_path(self, filename):
        """
        根据项目ID创建动态文件夹并存储文件
        """
        project_id_str = str(self.project.project_id)  # 获取项目ID
        # 文件路径为：project_files/<project_id>/<file_name>
        return os.path.join('project_files', project_id_str, filename)

    def save(self, *args, **kwargs):
        # 在保存之前设置 file 字段的 upload_to 路径
        self.file.name = self.get_upload_path(self.file_name)  # 通过 file_name 生成路径
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name

