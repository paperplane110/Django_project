'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-17 17:24:34
LastEditors: TianyuYuan
LastEditTime: 2021-03-17 20:14:11
'''
from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows':5,'placeholder':'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
        )


    class Meta:
        model = Topic
        fields = ['subject', 'message']