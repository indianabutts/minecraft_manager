from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from worlds.models import World

# Create your views here.
@login_required
def world_detail(request, world_id):
    user = request.user
    world = World.objects.get(pk=world_id)
    return render(request, "worlds/world_detail.html", {
        "world":world
    })
