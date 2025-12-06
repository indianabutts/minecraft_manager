from django.db import models
from core import models as cm
# Create your models here.
class Note(cm.ShareableModel):
    note = models.TextField()
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True, related_name="notes")
    world = models.ForeignKey("worlds.World", on_delete=models.CASCADE, blank=True, null=True, related_name="notes")
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE, blank=True, null=True, related_name="notes")
    
    
