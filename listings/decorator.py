from django.core.exceptions import PermissionDenied
from useraccounts.models import UserModel

def seller_authenticate(function):
    def wrap(request):
        account=request.user
        if account.is_seller == True:
            return function(request)
        else:
            raise PermissionDenied          ### raise mein return/render daal do

    return wrap