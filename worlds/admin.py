from django.contrib import admin
from worlds.models import World

# Register your models here.
@admin.register(World)
class WorldAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'version',
        'seed',
        'owner',
        'created_at',
        'updated_at'
    )

