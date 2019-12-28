from django import template

register = template.Library()
@register.filter(name='cut')  #decorator
def cut(value,arg):
    """cuts the number of arg from string"""
    return value.replace(arg,'')

#register.filter('cut',cut)
