from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import User
from .forms import EmployeeForm

from meetings.models import Meeting
from ai_services.models import AIResult

from accounts.decorators import admin_required

# -------------------------
# Login
# -------------------------

def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect("dashboard")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(request, "login.html")


# -------------------------
# Dashboard
# -------------------------

@login_required
def dashboard(request):

    total_employees = User.objects.filter(
        role="employee"
    ).count()

    total_meetings = Meeting.objects.count()

    total_reports = AIResult.objects.filter(
        processing_status="completed"
    ).count()

    pending_reports = AIResult.objects.filter(
        processing_status="pending"
    ).count()

    recent_meetings = Meeting.objects.order_by(
        "-created_at"
    )[:5]

    recent_reports = AIResult.objects.order_by(
        "-created_at"
    )[:5]

    recent_employees = User.objects.filter(
        role="employee"
    ).order_by(
        "-date_joined"
    )[:5]

    context = {

        "username": request.user.username,

        "role": request.user.role,

        "total_employees": total_employees,

        "total_meetings": total_meetings,

        "total_reports": total_reports,

        "pending_reports": pending_reports,

        "recent_meetings": recent_meetings,

        "recent_reports": recent_reports,

        "recent_employees": recent_employees,

    }

    return render(
        request,
        "dashboard.html",
        context
    )


# -------------------------
# Logout
# -------------------------

def logout_view(request):

    logout(request)

    return redirect("login")


# -------------------------
# Employee List
# -------------------------

@login_required
@admin_required
def employee_list(request):

    employees = User.objects.filter(
        role="employee"
    ).order_by(
        "first_name"
    )

    return render(
        request,
        "employees/employee_list.html",
        {
            "employees": employees
        }
    )


# -------------------------
# Add Employee
# -------------------------

@login_required
@admin_required
def employee_add(request):

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            employee = form.save(
                commit=False
            )

            password = form.cleaned_data.get(
                "password"
            )

            if password:
                employee.set_password(
                    password
                )

            employee.save()

            messages.success(
                request,
                "Employee added successfully."
            )

            return redirect(
                "employee_list"
            )

    else:

        form = EmployeeForm()

    return render(

        request,

        "employees/employee_add.html",

        {
            "form": form
        }

    )


# -------------------------
# Employee Details
# -------------------------

@login_required
def employee_detail(request, id):

    employee = get_object_or_404(
        User,
        id=id
    )

    return render(
        request,
        "employees/employee_detail.html",
        {
            "employee": employee
        }
    )


# -------------------------
# Edit Employee
# -------------------------

@login_required
@admin_required
def employee_edit(request, id):

    employee = get_object_or_404(
        User,
        id=id
    )

    if request.method == "POST":

        form = EmployeeForm(
            request.POST,
            request.FILES,
            instance=employee
        )

        if form.is_valid():

            employee = form.save(
                commit=False
            )

            password = form.cleaned_data.get(
                "password"
            )

            if password:
                employee.set_password(
                    password
                )

            employee.save()

            messages.success(
                request,
                "Employee updated successfully."
            )

            return redirect(
                "employee_list"
            )

    else:

        form = EmployeeForm(
            instance=employee
        )

    return render(

        request,

        "employees/employee_edit.html",

        {
            "form": form,
            "employee": employee
        }

    )


# -------------------------
# Delete Employee
# -------------------------

@login_required
@admin_required
def employee_delete(request, id):

    employee = get_object_or_404(
        User,
        id=id
    )

    if request.method == "POST":

        employee.delete()

        messages.success(
            request,
            "Employee deleted successfully."
        )

        return redirect(
            "employee_list"
        )

    return render(

        request,

        "employees/employee_delete.html",

        {
            "employee": employee
        }

    )