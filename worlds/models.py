from django.db import models
from django.utils.translation import gettext_lazy as _

from core import models as cm

# Create your models here.
class World(cm.UpdateableModel):
    class GameModeChoice(models.TextChoices):
        SURVIVAL = "Survival", _("Survival")
        CREATIVE = "Creative", _("Creative")
        HARDCORE = "Hardcore", _("Hardcore")
        
    name = models.CharField(max_length=255)
    world_file = models.FileField(blank=True, null=True)
    game_mode = models
    version = models.ForeignKey("core.Version", on_delete=models.SET_NULL, null=True, related_name="worlds")
    seed = models.IntegerField(blank=True, null=True)
    active = models.BooleanField(default=True)
    owner = models.ForeignKey("mc_user.MCUser", on_delete=models.SET_NULL, null=True, related_name="worlds")
    game_mode = models.CharField(max_length=32, choices=GameModeChoice.choices, default=GameModeChoice.SURVIVAL)

