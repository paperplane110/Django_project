'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-19 14:38:07
LastEditors: TianyuYuan
LastEditTime: 2021-03-19 14:41:42
'''
from django import template

register = template.Library()

@register.filter
def field_type(bound_field):
    return bound_field.field.widget.__class__.__name__

@register.filter
def input_class(bound_field):
    css_class = ''
    if bound_field.form.is_bound:
        if bound_field.errors:
            css_class = 'is-invalid'
        elif field_type(bound_field) != 'PasswordInput':
            css_class = 'is-valid'
    return 'form-control {}'.format(css_class)