from django.db import models
from core import models as cm

# Create your models here.

class Project(cm.ShareableModel):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project_type = models.ForeignKey('projects.ProjectType', on_delete=models.SET_NULL, null=True)
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True)
    
class ProjectType(cm.UpdateableModel):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)

