from django.contrib import admin
from projects.models import Project, ProjectType, Task
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

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'name',
        'description',
        'project',
        'owner',
        'complete'
    )
