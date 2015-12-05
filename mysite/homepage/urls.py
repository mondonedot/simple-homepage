from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^modify_bookmarks/$', views.modify_bookmarks, name='modify_bookmarks'),
	url(r'^save_notepad/$', views.save_notepad, name='save_notepad'),
	url(r'^preferences/$', views.PreferencesView.as_view(), name='preferences'),
	url(r'^modify_preferences/$', views.modify_preferences, name='modify_preferences'),
]
