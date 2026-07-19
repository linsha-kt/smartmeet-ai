from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps


def admin_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if request.user.role != "admin":

            messages.error(
                request,
                "Access Denied! Only administrators can perform this action."
            )

            return redirect("dashboard")

        return view_func(request, *args, **kwargs)

    return wrapper