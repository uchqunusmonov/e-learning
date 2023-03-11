from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    def has_object_permission(self, requests, view, obj):
        return obj.students.filter(id=requests.user.id).exists()
