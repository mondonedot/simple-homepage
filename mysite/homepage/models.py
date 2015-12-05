from django.db import models

# Create your models here.
class Bookmark(models.Model):
	'''
	Model that holds the name of a bookmark and the corresponding url.
	'''

	bookmark_name = models.CharField(max_length=200)
	bookmark_url = models.CharField(max_length=1000)

	def __unicode__(self):
		'''
		Returns the name of the bookmark for printing purposes.
		'''
		return self.bookmark_name

class Widget(models.Model):
	'''
	Model that keeps track of what widgets the user has selected.
	'''

	widget_name = models.CharField(max_length=200)
	widget_code = models.CharField(max_length=40000)

	def __unicode__(self):
		'''
		Returns the name of the widget for printing purposes.
		'''
		return self.widget_name

class Notepad(models.Model):
	'''
	Model for the notepad on the website with different tabs.
	Saves the text for a specific tab.
	'''

	tab_name = models.CharField(max_length=25)
	tab_data = models.TextField(blank=True)

	def __unicode__(self):
		'''
		Returns the name of the tab for printing purposes.
		'''
		return self.tab_name

class Preferences(models.Model):
	'''
	Holds all the different customizations that can be made on the website.
	'''
	
	nickname = models.CharField(max_length=50) 
	primary_color = models.CharField(max_length=6)
	secondary_color = models.CharField(max_length=6)
	banner_text = models.CharField(max_length=50)

	def __unicode__(self):
		'''
		Returns the nickname of the person for printing purposes.
		'''
		return self.nickname
