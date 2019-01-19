from django import template

register = template.Library()

@register.filter(name='rep_slash')
def rep_slash(value):
    if '-' in value:
        return value.replace('-','/',1).upper()
    elif ',' in value:
        return value.replace(',','/',1).upper()
    elif ' ' in value:
        return value.replace(' ','/',1).upper()
    elif '.' in value:
        return value.replace('.','/',1).upper()

@register.filter(name='nam_cap')
def nam_cap(value):
    return value.title()
