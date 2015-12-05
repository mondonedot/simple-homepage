from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .models import Bookmark, Widget, Notepad, Preferences
import json

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'homepage/index.html'
	
	def get_queryset(self):
		return None

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['bookmark_list'] = Bookmark.objects.all()
		context['widget_list'] = Widget.objects.all()
		context['notepad_data'] = Notepad.objects.all()
		context['preferences'] = Preferences.objects.all()
		return context

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(IndexView, self).dispatch(*args, **kwargs)

@csrf_exempt
def modify_bookmarks(request):
	'''
	Process a request that was posted through the modify bookmark form.
	Either adds or deletes a bookmark.
	'''

	if request.POST['bookmark_request'] == 'add':
		name = request.POST['bookmark_name']
		url = request.POST['bookmark_url']
		
		new_bookmark = Bookmark(bookmark_name=name, bookmark_url=url)
		new_bookmark.save()
	elif request.POST['bookmark_request'] == 'delete':
		key = int(request.POST['key'])
		curr_bookmark = Bookmark.objects.get(pk=key)
		curr_bookmark.delete()

	return HttpResponseRedirect('/homepage/')

@csrf_exempt
def save_notepad(request):
	'''
	Saves the current state of the specified notepad tab.
	'''
	
	content = request.POST['content']
	content_tab = request.POST['content_tab']

	#Get the corresponding notepad object based on what tab is being saved and update it.
	Notepad.objects.filter(tab_name=content_tab).update(tab_data=content)
	
	#Return data for use if needed.
	response_data = {}
	response_data['text'] = content
	return HttpResponse(json.dumps(response_data), content_type="application/json")

class PreferencesView(generic.ListView):
	template_name = 'homepage/preferences.html'
	
	def get_queryset(self):
		return None

	def get_context_data(self, **kwargs):
		context = super(PreferencesView, self).get_context_data(**kwargs)
		context['bookmark_list'] = Bookmark.objects.all()
		context['widget_list'] = Widget.objects.all()
		context['notepad_data'] = Notepad.objects.all()
		context['preferences'] = Preferences.objects.all()
		return context

	@csrf_exempt
	def dispatch(self, *args, **kwargs):
		return super(PreferencesView, self).dispatch(*args, **kwargs)

@csrf_exempt
def modify_preferences(request):
	'''
	Process a request that was posted from the preferences page.
	Changes the specific preference that the user wants to change.
	'''

	if request.POST['save_preferences'] == 'colors_and_text':
		primary_color = request.POST['primary_color']
		secondary_color = request.POST['secondary_color']
		banner_text = request.POST['banner_text']
		Preferences.objects.all().update(primary_color = primary_color, secondary_color = secondary_color, banner_text = banner_text)	

	if request.POST['save_preferences'] == 'create_widget':
		widget_name = request.POST['widget_name']
		widget_code = request.POST['widget_code']
		new_widget = Widget(widget_name=widget_name, widget_code=widget_code)
		new_widget.save()

	if request.POST['save_preferences'] == 'delete_widget':
		key = int(request.POST['key'])
		Widget.objects.get(pk=key).delete()

	if request.POST['save_preferences'] == 'create_tab':
		tab_name = request.POST['tab_name']
		new_tab = Notepad(tab_name=tab_name)
		new_tab.save()

	if request.POST['save_preferences'] == 'delete_tab':
		key = request.POST['key']
		Notepad.objects.get(pk=key).delete()

	return HttpResponseRedirect('/homepage/preferences/')
	#Return data for use if needed.
	#response_data = {}
	#response_data['text'] = 'blank'
	#return HttpResponse(json.dumps(response_data), content_type="application/json")

