'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-18 11:27:52
LastEditors: TianyuYuan
LastEditTime: 2021-03-18 16:29:14
'''
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})