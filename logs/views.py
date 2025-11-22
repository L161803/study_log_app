from django.shortcuts import render, redirect
from .models import StudyLog
from .forms import StudyLogForm

# Create your views here.
def index(request):
    if request.method == "POST":
        form = StudyLogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = StudyLogForm()

    logs = StudyLog.objects.all().order_by("-created_at")

    return render(request, "logs/index.html",{
        "logs": logs,
        "form": form
    })
