from django.shortcuts import render

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    user = request.user
    worlds = user.worlds.all()
    return render(request, "core/base.html", {
        "worlds":worlds
    })
