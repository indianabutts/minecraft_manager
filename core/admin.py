from django.contrib import admin
from core.models import Version
# Register your models here.
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        'edition',
        'version_number'
    )
