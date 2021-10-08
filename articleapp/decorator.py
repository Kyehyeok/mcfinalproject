# from django.contrib.auth.models import User
# from django.http import HttpResponseForbidden
#
# from articleapp.models import FoodDetail
#
#
# def food_ownership_required(func):
#     def decorated(request, *args, **kwargs):
#         fooddetail = FoodDetail.objects.get(pk=kwargs['pk'])
#         if not fooddetail.code == request.code:
#             return HttpResponseForbidden()
#         return func(request, *args ,**kwargs)
#     return decorated