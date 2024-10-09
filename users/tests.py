from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()

class UserAuthTests(TestCase):

    def setUp(self):
        self.user_data = {
            'name': 'Test User',
            'school': 'Fuzhou University',
            'student_id': 'T123456789',
            'email': 'testuser@fzu.edu.com',
            'password': 'testpassword',
            'password_confirm': 'testpassword',
        }
        self.registration_url = reverse('register')  # 假设你的注册视图URL名称是'register'
        self.login_url = reverse('login')  # 假设你的登录视图URL名称是'login'

    def test_user_registration(self):
        # 测试用户注册
        response = self.client.post(self.registration_url, self.user_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)  # 确保返回201状态
        self.assertTrue(User.objects.filter(email=self.user_data['email']).exists())  # 确保用户被创建

    def test_user_login(self):
        # 首先要创建用户
        user = User.objects.create_user(
            student_id=self.user_data['student_id'],
            name=self.user_data['name'],
            school=self.user_data['school'],
            email=self.user_data['email'],
            password=self.user_data['password'],
        )
        user.is_active = True  # 激活用户
        user.save()

        # 测试用户登录
        response = self.client.post(self.login_url, {
            'email': self.user_data['email'],
            'password': self.user_data['password'],
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)  # 确保返回200状态
        self.assertContains(response, 'Login successful')  # 确保登录成功消息

    def test_login_with_invalid_credentials(self):
        # 测试使用无效凭据登录
        response = self.client.post(self.login_url, {
            'email': 'wrongemail@example.com',
            'password': 'wrongpassword',
        }, content_type='application/json')

        # 检查状态码为401
        self.assertEqual(response.status_code, 401)  # 确保返回401状态

        # 检查错误消息
        response_data = response.json()  # 获取响应的JSON数据
        self.assertEqual(response_data['error'], 'Invalid email or password')  # 确保错误消息
