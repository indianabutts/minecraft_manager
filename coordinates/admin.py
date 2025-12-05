from django.contrib import admin
from coordinates.models import Coordinate
# Register your models here.
@admin.register(Coordinate)
class CoordinateAdmin(admin.ModelAdmin):
    list_display = (
        'coordinates',
        'description',        
        'world',
        'project',
        'owner',
        'private',
        'created_at',
        'updated_at'
    )
