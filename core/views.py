from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    worlds = user.worlds
    active_worlds = worlds.filter(active=True)
    active_tasks = user.tasks.filter(complete=False)
    return render(request, "core/base.html", {
        "worlds":worlds.all(),
        "active_worlds":active_worlds,
        "active_tasks": active_tasks,
        "user":user
    })
