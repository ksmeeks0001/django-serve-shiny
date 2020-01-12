from django.contrib import admin
from .models import ActiveShiny, ShinyUserHash


# Register your models here.
admin.site.register(ActiveShiny)
admin.site.register(ShinyUserHash)