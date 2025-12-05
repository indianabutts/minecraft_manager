from django.db import models
from core import models as cm

# Create your models here.
class World(cm.UpdateableModel):
    name = models.CharField(max_length=255)
    world_file = models.FileField(blank=True, null=True)
    version = models.ForeignKey("core.Version", on_delete=models.SET_NULL, null=True)
    seed = models.IntegerField(blank=True, null=True)
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True)
    

