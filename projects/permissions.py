from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    只有项目的发布者或管理员有权限修改或删除项目。
    """
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user or request.user.is_admin
