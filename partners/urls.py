from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # 其他URL路由
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    path('projects/', include('projects.urls')),
    path('chat/', include('chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
