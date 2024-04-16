from rest_framework import permissions


class OwnerFullAccess(permissions.BasePermission):
    """ GUEST - только просмотр, ADMIN - или OWNER все методы """
    def has_permission(self, request, view):
        return (request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (obj.user == request.user)
