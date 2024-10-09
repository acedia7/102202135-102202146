from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectMemberViewSet, ProjectFileViewSet,ProjectSearchViewSet
from .views import recommend_students, recommend_teachers

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'members', ProjectMemberViewSet, basename='member')
router.register(r'files', ProjectFileViewSet, basename='file')
router.register(r'search', ProjectSearchViewSet, basename='project-search')


urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:project_id>/recommend_students/', recommend_students, name='recommend_students'),
    path('projects/<int:project_id>/recommend_teachers/', recommend_teachers, name='recommend_teachers'),
]


