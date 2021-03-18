'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-18 11:27:52
LastEditors: TianyuYuan
LastEditTime: 2021-03-18 16:50:07
'''
from django.contrib.auth.forms import UserCreationForm
from ..forms import SignUpForm
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse, resolve
from ..views import signup

# Create your tests here.
class SignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        self.response = self.client.get(url)

    def test_signup_status_code(self):
        self.assertEquals(200, self.response.status_code)

    def test_signup_url_resolves_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)

    def test_csrf(self):
        self.assertContains(self.response,'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form,SignUpForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input', 5)
        self.assertContains(self.response, 'type="text"', 1)
        self.assertContains(self.response, 'type="email"',1)
        self.assertContains(self.response, 'type="password"',2)

class SuccessfulSignUpTest(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {
            'username':'chwang',
            'email':"chwang@qq.com",
            'password1':'wang3213645',
            'password2':'wang3213645',
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        self.assertRedirects(self.response,self.home_url)

    def test_user_creation(self):
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)

class InvalidSignUpTests(TestCase):
    def setUp(self):
        url = reverse('signup')
        data = {}
        self.response = self.client.post(url,data)
    
    def test_signup_status_code(self):
        self.assertEquals(200,self.response.status_code)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
    
    def test_dont_create_user(self):
        self.assertFalse(User.objects.exists())