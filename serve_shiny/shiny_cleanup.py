import django
from django.conf import settings
from importlib.machinery import SourceFileLoader
from django.utils import timezone
from os import makedirs
from pathlib import Path
from shutil import rmtree
import sys




def clean_up_shiny():
	"""Remove all apps in shiny directory that are expired."""
	print("in cleanup func")
	expired_sessions = ActiveShiny.objects.filter(expiration__lt = timezone.now())
	for session in expired_sessions:
		session_dir = Path(settings.SHINY_SERVER_DIRECTORY, session.project_dir)
		if session_dir.exists() and session_dir.is_dir():
			rmtree(session_dir)
		session.delete()

if __name__ == "__main__":
	user_settings = SourceFileLoader("settings", sys.argv[1]).load_module()
	settings.configure(DATABASES=user_settings.DATABASES,
		SHINY_SERVER_DIRECTORY=user_settings.SHINY_SERVER_DIRECTORY,
		INSTALLED_APPS=user_settings.INSTALLED_APPS,
		TIME_ZONE=user_settings.TIME_ZONE,
		USE_TZ=user_settings.USE_TZ)
	django.setup()
	from serve_shiny.models import ActiveShiny
	clean_up_shiny()
	
