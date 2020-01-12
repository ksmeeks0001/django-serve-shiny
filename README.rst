===
django-serve-shiny
===

Django application to server dynamic R-Shiny Apps

Quick Start
-----------

1. Add 'serve_shiny' to INSTALLED_APPS in settings.py:

    INSTALLED_APPS = [
	...
	'serve_shiny',
    ]

2. Include serve_shiny urls in project urls.py:

	path('serve_shiny', include('serve_shiny.urls')),

3. Run 'python manage.py migrate' to add models to database


