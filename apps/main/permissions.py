from strawberry.permission import BasePermission

class IsOwner(BasePermission):
    message = "You must be the staff to perform this action."

    def has_permission(self, source, info, **kwargs):
        allowed_methods = ['list', 'create', 'retrieve', 'update', 'partial_update', 'destroy']
        request_method = info.context.request.method.lower()

        if (info.field_name in ['list', 'retrieve'] or request_method == 'get') and not info.context.user.is_staff:
            return False
        elif (info.field_name in allowed_methods or request_method == 'put', 'patch', 'post', 'delete') and info.context.user.is_staff:
            return True
        else:
            return False
    
    # def has_object_permission(self, request, info, obj):
    #     if request.user.is_staff:
    #         return True
    #     else:
    #         return False