# mutual_funds/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    """Returns the value for a given key from a dictionary."""
    return dictionary.get(key)
