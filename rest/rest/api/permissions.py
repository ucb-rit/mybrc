from rest_framework import permissions
from .models import *


class UserOwnershipPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # user = request.user
        if isinstance(obj, User):
            if obj is request.user:
                return True
        elif isinstance(obj, Job):
            if obj.userid == request.user.userid:
                return True
        elif isinstance(obj, Account):
            if request.user in obj.users:
                return True
        elif isinstance(obj, UserAccountAssociation):
            if obj.userid == request.user.userid:
                return True
        else:
            return False
