from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        else:
            return func(request, *args, **kwargs)
    return decorated


    # def get(self, *args, **kwargs):
    #     if self.requset.user.is_authenticated and self.get_object() == self.request.user :
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()
    #
    # def post(self, *args, **kwargs):
    #     if self.requset.user.is_authenticated and self.get_object() == self.request.user :
    #         return super().get(*args, **kwargs)
    #     else:
    #         return HttpResponseForbidden()