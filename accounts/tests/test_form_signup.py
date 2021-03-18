'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-18 16:49:56
LastEditors: TianyuYuan
LastEditTime: 2021-03-18 17:16:00
'''
from django.test import TestCase
from .. forms import SignUpForm

class SignUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SignUpForm()
        expected = ['username', 'email', 'password1', 'password2']
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)