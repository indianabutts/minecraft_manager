from django.db import models
from core import models as cm

# Create your models here.

class Project(cm.ShareableModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project_type = models.ForeignKey('projects.ProjectType', on_delete=models.SET_NULL, null=True, related_name="projects")
    world = models.ForeignKey("worlds.World", on_delete=models.SET_NULL, null=True, related_name="projects")
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True, related_name="projects")

    def __str__(self):
        return f"[{self.project_type.name}] {self.world} / {self.name}"
    
class ProjectType(cm.UpdateableModel):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"

class Task(cm.ShareableModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, related_name="tasks")
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True, related_name="tasks")
    complete = models.BooleanField(default=False)

    def __str__(self):
        return f"[{self.project.name}] {self.name}"
