from django.contrib import admin
from projects.models import Project, ProjectType
# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'project_type',
        'owner',
        'private',
        'created_at',
        'updated_at'
    )

@admin.register(ProjectType)
class ProjectTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description'
    )
