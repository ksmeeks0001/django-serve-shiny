from django.conf import settings
from django.shortcuts import render
from django.http import Http404, JsonResponse
from django.utils import timezone
from .models import ShinyUserHash, ActiveShiny
from .utils import  generate_shiny
from secrets import token_hex
from datetime import timedelta
from importlib.machinery import SourceFileLoader


def hash_view(request, id):
	try:
		shinyuser = ShinyUserHash.objects.get(user__id=id)
	except ShinyUserHash.DoesNotExist:
		raise Http404("Not Found")
	hash = shinyuser.user_hash
	try:
		context_module = SourceFileLoader("context",settings.SHINY_CONTEXT_MODULE).load_module()
		shiny_context = context_module.shiny_context(request)
	except Exception as e: #setting not configured / file not found / function improperly named
		print(e)
		shiny_context = {}
	generate_shiny(hash, shiny_context)
	shinyuser.user_hash = token_hex(16)
	shinyuser.save()
	template_name = 'serve_shiny/shiny_wrapper.html'
	context = {'hash': hash, "shiny_url": settings.SHINY_SERVER_URL}
	return render(request, template_name, context)

def update_connection(request):
	if request.method != 'POST':
		return HttpResponseNotFound("NOT FOUND")
	#post data coming in strange from javascript
	hash = request.POST.get(" name")[10:42]
	if hash is None or hash == "":
		return HttpResponseNotFound("Not Found")
	now = timezone.now()
	allowance = timedelta(minutes=10)
	try:
		is_active = ActiveShiny.objects.get(project_dir = hash)
	except ActiveShiny.DoesNotExist:
		is_active = False
	if is_active:
		is_active.expiration = now + allowance
		is_active.save(update_fields = ['expiration'])
	else:
		activate = ActiveShiny(project_dir = hash, expiration = (now + allowance) )
		activate.save() 
	return JsonResponse({'status': 'updated'})

