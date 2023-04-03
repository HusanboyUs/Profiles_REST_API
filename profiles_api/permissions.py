from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit thier own profile only"""

    def had_object_permission(self,request,view,obj):
        """Check user is tring to edit their own profile"""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id