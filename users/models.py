from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import os
import uuid

def user_avatar_path(instance, filename):
    # 提取文件扩展名
    ext = filename.split('.')[-1]
    # 使用 UUID 生成唯一文件名，并保持文件扩展名
    filename = f"{uuid.uuid4()}.{ext}"
    # 返回保存路径，路径中包含 avatars 文件夹和用户ID
    return os.path.join('avatars', str(instance.id), filename)


class UserManager(BaseUserManager):
    def create_user(self, student_id, name, school, email, password=None):
        if not student_id:
            raise ValueError('Students must have a student ID')
        if not email:
            raise ValueError('Users must have an email address')
        email = self.normalize_email(email)
        user = self.model(student_id=student_id, name=name, school=school, email=email)
        user.set_password(password)
        user.is_active = False  # 用户未验证邮箱前不激活账户
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, name, school, email, password=None):
        user = self.create_user(student_id, name, school, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    student_id = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, default='')  # 邮箱唯一
    email_verified = models.BooleanField(default=False)  # 标记邮箱是否验证
    is_active = models.BooleanField(default=False)  # 初始账户不激活，等待验证
    is_admin = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)  # 新增字段，判断是否为老师

    # 新增字段
    major = models.CharField(max_length=255, blank=True, null=True)  # 专业
    phone = models.CharField(max_length=20, blank=True, null=True)  # 电话号码
    interests = models.TextField(blank=True, null=True)  # 兴趣领域
    available_time = models.TextField(blank=True, null=True)  # 空闲时间
    avatar = models.ImageField(upload_to=user_avatar_path, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # 使用教育邮箱作为登录标识
    REQUIRED_FIELDS = ['student_id', 'name', 'school']

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_admin



