from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Task
from .forms import TaskForm

from accounts.decorators import admin_required


# -------------------------
# Task List
# -------------------------

@login_required
def task_list(request):

    if request.user.role == "admin":

        tasks = Task.objects.all().order_by("-created_at")

    else:

        tasks = Task.objects.filter(
            assigned_to=request.user
        ).order_by("-created_at")

    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks
        }
    )


# -------------------------
# Add Task
# -------------------------

@login_required
@admin_required
def task_add(request):

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Task created successfully."
            )

            return redirect("task_list")

    else:

        form = TaskForm()

    return render(
        request,
        "tasks/task_add.html",
        {
            "form": form
        }
    )


# -------------------------
# Edit Task
# -------------------------

@login_required
@admin_required
def task_edit(request, id):

    task = get_object_or_404(
        Task,
        id=id
    )

    if request.method == "POST":

        form = TaskForm(
            request.POST,
            instance=task
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Task updated successfully."
            )

            return redirect("task_list")

    else:

        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/task_edit.html",
        {
            "form": form,
            "task": task
        }
    )


# -------------------------
# Delete Task
# -------------------------

@login_required
@admin_required
def task_delete(request, id):

    task = get_object_or_404(
        Task,
        id=id
    )

    if request.method == "POST":

        task.delete()

        messages.success(
            request,
            "Task deleted successfully."
        )

        return redirect("task_list")

    return render(
        request,
        "tasks/task_delete.html",
        {
            "task": task
        }
    )