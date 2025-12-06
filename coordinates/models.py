from django.db import models
from core import models as cm
# Create your models here.

class Coordinate(cm.ShareableModel):
    description = models.TextField(blank=True)
    screenshot = models.ImageField(blank=True)
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    z_coordinate = models.IntegerField() 
    world = models.ForeignKey("worlds.World", on_delete=models.SET_NULL, null=True, related_name="coordinates")
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True, related_name="coordinates")
    project = models.ForeignKey("projects.Project", on_delete=models.SET_NULL, null=True, blank=True, related_name="coordinates")
    
    @property
    def coordinates(self):
        return {
            "x": self.x_coordinate,
            "y": self.y_coordinate,
            "z": self.z_coordinate
        }

    def __str__(self):
        return f"{self.world} / {self.coordinates}"
