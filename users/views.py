import datetime
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from rest_framework.permissions import IsAuthenticated

from .models import User
import random
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view, permission_classes

# 邮箱验证码缓存字典
email_verification_codes = {}

from django.contrib.auth import get_user_model
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

User = get_user_model()  # 获取自定义的用户模型

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        school = data.get('school')
        student_id = data.get('student_id')
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        email = data.get('email')  # 获取教育邮箱

        # 验证邮箱格式
        if not email or '@' not in email or 'edu' not in email:
            return JsonResponse({'error': 'Invalid email'}, status=400)

        # 验证字段是否为空
        if not all([name, school, student_id, password, password_confirm, email]):
            return JsonResponse({'error': 'All fields are required'}, status=400)

        # 验证密码是否一致
        if password != password_confirm:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)

        # 检查用户是否已经存在
        try:
            existing_user = User.objects.get(email=email)
            # 如果用户已经存在但未激活
            if not existing_user.is_active:
                return JsonResponse({'message': 'Account exists but not activated. Please verify your email.'}, status=200)
            else:
                return JsonResponse({'error': 'Account already exists and is active.'}, status=400)
        except User.DoesNotExist:
            # 用户不存在，继续创建新用户
            is_teacher = student_id.startswith('T')  # 如果 student_id 以 'T' 开头，则是老师

            # 创建用户但不激活账户
            user = User.objects.create_user(student_id=student_id, name=name, school=school, email=email, password=password)
            user.is_teacher = is_teacher  # 设置用户身份
            user.is_active = False  # 标记为未激活
            user.save()

            return JsonResponse({'message': 'Registration successful. Please verify your email.'}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def send_verification_code(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')

        # 验证邮箱格式
        if not email or '@' not in email or 'edu' not in email:
            return JsonResponse({'error': 'Invalid email'}, status=400)

        # 生成验证码
        verification_code = random.randint(100000, 999999)
        current_time = datetime.datetime.now()

        # 保存验证码和生成时间
        email_verification_codes[email] = {
            'code': verification_code,
            'timestamp': current_time
        }

        try:
            # 发送验证码邮件
            send_mail(
                'Your Verification Code',
                f'Your verification code is {verification_code}.The verification code will expire in 15 minutes.',
                '1335357913@qq.com',  # 发件人
                [email],  # 收件人
                fail_silently=False,
            )
            return JsonResponse({'message': 'Verification code sent'}, status=200)
        except BadHeaderError:
            return JsonResponse({'error': 'Invalid header found.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def verify_email(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        code = data.get('code')

        # 验证验证码是否存在
        if email in email_verification_codes:
            stored_data = email_verification_codes[email]
            stored_code = stored_data['code']
            timestamp = stored_data['timestamp']

            # 计算当前时间和生成时间的时间差
            current_time = datetime.datetime.now()
            time_diff = current_time - timestamp

            # 检查验证码是否过期（15分钟）
            if time_diff.total_seconds() > 15 * 60:
                return JsonResponse({'error': 'Verification code expired'}, status=400)

            # 检查验证码是否匹配
            if stored_code == int(code):
                # 激活账户
                user = User.objects.get(email=email)
                user.is_active = True
                user.email_verified = True
                user.save()

                # 清除已使用的验证码
                del email_verification_codes[email]

                return JsonResponse({'message': 'Email verified, registration completed'}, status=200)
            else:
                return JsonResponse({'error': 'Invalid verification code'}, status=400)

        return JsonResponse({'error': 'No verification code found for this email'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        # 尝试验证用户
        user = authenticate(request, username=email, password=password)
        # print(user)  # 调试输出

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return JsonResponse({'message': 'Login successful'}, status=200)
            else:
                return JsonResponse({'error': 'Account not active. Please verify your email.'}, status=403)
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user

        # 更新用户信息
        user.major = data.get('major', user.major)
        user.phone = data.get('phone', user.phone)
        user.interests = data.get('interests', user.interests)
        user.available_time = data.get('available_time', user.available_time)

        user.save()

        return JsonResponse({'message': 'Profile updated successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@csrf_exempt  # 根据需要免除 CSRF 检查
def get_user_profile(request):
    if request.method == 'GET':
        user = request.user

        # 返回用户的所有信息
        user_info = {
            'name': user.name,
            'email': user.email,
            'student_id': user.student_id,
            'school': user.school,
            'major': user.major,
            'phone': user.phone,
            'interests': user.interests,
            'available_time': user.available_time,
            'avatar': request.build_absolute_uri(user.avatar.url).replace('http://', 'https://') if user.avatar else None
        }

        return JsonResponse(user_info, status=200)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@api_view(['POST'])
@permission_classes([IsAuthenticated])  # 确保用户已认证
@csrf_exempt  # 视需求决定是否跳过CSRF验证
def upload_avatar(request):
    if request.method == 'POST' and request.FILES.get('avatar'):
        user = request.user
        avatar = request.FILES['avatar']  # 从请求中获取上传的文件

        # 删除旧头像（可选，避免存储过多文件）
        if user.avatar:
            user.avatar.delete(save=False)

        # 保存新头像
        user.avatar = avatar
        user.save()

        return JsonResponse({'message': 'Avatar uploaded successfully'}, status=200)

    return JsonResponse({'error': 'Invalid request or missing file'}, status=400)