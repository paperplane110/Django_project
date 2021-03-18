'''
Description: 
version: 
Author: TianyuYuan
Date: 2021-03-16 14:32:06
LastEditors: TianyuYuan
LastEditTime: 2021-03-17 20:06:58
'''
from .forms import NewTopicForm
from django.shortcuts import redirect, get_object_or_404, render
from django.http import HttpResponse,Http404
from .models import Board, User, Post, Topic

# Create your views here.
def home(request):
    boards = Board.objects.all()
    return render(request,'home.html',{'boards':boards})

def board_topics(request,pk):
    board = get_object_or_404(Board,pk=pk)
    # try:    
    #     board = Board.objects.get(pk=pk)
    # except Board.DoesNotExist:
    #     raise Http404
    return render(request,'topics.html',{'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board,pk=pk)
    user = User.objects.first() # todo get the current logged in user

    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message = form.cleaned_data.get('message'),
                topic = topic,
                created_by = user
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request,'new_topic.html',{'board':board,'form':form})