from django.conf import settings
from django.template import Template, Context
from os import makedirs, path
from .models import ActiveShiny


def generate_shiny(hash, shiny_context):
	"""populate the shiny app"""
	makedirs(path.join(settings.SHINY_SERVER_DIRECTORY,hash))
	#context from function overwrites any in settings file
	if shiny_context:
		context = Context(shiny_context)
	else:
		context = Context(settings.SHINY_CONTEXT)
	
	if type(settings.SHINY_TEMPLATE_FILE) == type(str()):
		with open(settings.SHINY_TEMPLATE_FILE, 'r') as file:
			shiny_template = Template(file.read())
		with open(path.join(settings.SHINY_SERVER_DIRECTORY , hash , "shiny.R"), 'w') as shiny_application:
			shiny_application.write(shiny_template.render(context))
	else:
		#if SHINY_TEMPLATE_FILE is list of files then SHINY_TEMPLATE_DIRECTORY should be defined
		for shiny_file in settings.SHINY_TEMPLATE_FILE:
			with open(path.join(settings.SHINY_TEMPLATE_DIRECTORY,shiny_file), 'r') as file:
				shiny_template = Template(file.read())
			with open(path.join(settings.SHINY_SERVER_DIRECTORY , hash , shiny_file), 'w') as shiny_application:
				shiny_application.write(shiny_template.render(context))




	
	
	
