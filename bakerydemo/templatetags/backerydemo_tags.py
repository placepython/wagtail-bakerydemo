import os

from django import template

register = template.Library()


@register.simple_tag
def environ(variable_name, default=None):
    return os.getenv(variable_name, default)
