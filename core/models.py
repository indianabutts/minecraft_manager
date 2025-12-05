from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UpdateableModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ShareableModel(UpdateableModel):
    private = models.BooleanField(default=True)

    class Meta:
        abstract = True
        
class Version(UpdateableModel):
    class EditionChoice(models.TextChoices):
        JAVA = "Java", _("Java")
        BEDROCK = "Bedrock", _("Bedrock")

    version_number = models.CharField(max_length=16)
    edition = models.CharField(max_length=16, choices=EditionChoice.choices, default=EditionChoice.JAVA)
