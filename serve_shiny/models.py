from django.db import models
from django.contrib.auth.models import User



class ShinyUserHash(models.Model):
    user_hash = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class ActiveShiny(models.Model):
    project_dir = models.CharField(max_length = 32)
    expiration = models.DateTimeField()
	
    def __str__(self):
        return "Active Shiny Session {} expires {}".format(self.project_dir, self.expiration)