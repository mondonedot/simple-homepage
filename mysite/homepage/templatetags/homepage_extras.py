from django import template

register = template.Library()

@register.filter
def get_object(notepad_data, key):
	'''
	Register a template filter to get a notepad tab based on the name.
	'''
	return notepad_data.filter(tab_name=key)
