from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            groups = None
            if request.user.groups.exists():
                groups = request.user.groups.all()
                if groups is not None:
                    for group in groups:
                        if group.name in allowed_roles:
                            return view_func(request, *args, **kwargs)
                        else:
                            return HttpResponseForbidden()

            else:
                return HttpResponseForbidden()
        return wrapper_func
    return decorator