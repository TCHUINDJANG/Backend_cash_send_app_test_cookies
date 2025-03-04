class AuthorTransactionPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ["GET", "OPTIONS" , "HEAD"]:
            return True
        if  request.method in ["PUT" ,  "PATCH" , "DELETE"]:
            if obj.user == request.user:
                return True
            return False