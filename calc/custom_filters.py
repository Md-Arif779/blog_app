from django import template
from django.utils.text import Truncator

register = template.Library()

@register.filter
def truncate_words(value, num_words):
    return Truncator(value).words(num_words, html=True, truncate=' ...')
