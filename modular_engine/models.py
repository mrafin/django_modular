from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    version = models.CharField(max_length=20)
    installed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} (v{self.version})"