from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Meeting
from .forms import MeetingForm

from accounts.decorators import admin_required


@login_required
def meeting_list(request):

    search = request.GET.get("search")

    meetings = Meeting.objects.all().order_by("-meeting_date")

    if search:

        meetings = meetings.filter(
            title__icontains=search
        )

    paginator = Paginator(meetings, 5)

    page = request.GET.get("page")

    meetings = paginator.get_page(page)

    context = {
        "meetings": meetings,
        "search": search,
    }

    return render(
        request,
        "meetings/meeting_list.html",
        context
    )


@login_required
@admin_required
def meeting_add(request):

    if request.method == "POST":

        form = MeetingForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            meeting = form.save(commit=False)

            meeting.created_by = request.user

            meeting.save()

            form.save_m2m()

            messages.success(
                request,
                "Meeting created successfully."
            )

            return redirect("meeting_list")

    else:

        form = MeetingForm()

    return render(
        request,
        "meetings/meeting_add.html",
        {
            "form": form
        }
    )


@login_required
def meeting_detail(request, id):

    meeting = get_object_or_404(
        Meeting,
        id=id
    )

    return render(
        request,
        "meetings/meeting_detail.html",
        {
            "meeting": meeting
        }
    )


@login_required
@admin_required
def meeting_edit(request, id):

    meeting = get_object_or_404(
        Meeting,
        id=id
    )

    if request.method == "POST":

        form = MeetingForm(
            request.POST,
            request.FILES,
            instance=meeting
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Meeting updated successfully."
            )

            return redirect("meeting_list")

    else:

        form = MeetingForm(
            instance=meeting
        )

    return render(
        request,
        "meetings/meeting_edit.html",
        {
            "form": form,
            "meeting": meeting
        }
    )


@login_required
@admin_required
def meeting_delete(request, id):

    meeting = get_object_or_404(
        Meeting,
        id=id
    )

    if request.method == "POST":

        meeting.delete()

        messages.success(
            request,
            "Meeting deleted successfully."
        )

        return redirect("meeting_list")

    return render(
        request,
        "meetings/meeting_delete.html",
        {
            "meeting": meeting
        }
    )