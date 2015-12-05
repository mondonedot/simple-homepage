from django.contrib import admin

from .models import Bookmark, Widget, Notepad, Preferences

# Register your models here.
admin.site.register(Bookmark)
admin.site.register(Widget)
admin.site.register(Notepad)
admin.site.register(Preferences)
