from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('verify_email/', views.verify_email, name='verify_email'),
    path('login/', views.login, name='login'),  # 新增登录路径
    path('update_profile/', views.update_profile, name='update_profile'),
    path('get_user_profile/', views.get_user_profile, name='get_user_profile'),
    path('upload_avatar/', views.upload_avatar, name='upload_avatar'),
]
