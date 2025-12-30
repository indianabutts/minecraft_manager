from django.urls import path

from worlds import views

urlpatterns = [
    path("<int:world_id>", views.world_detail, name="world_detail")
]
