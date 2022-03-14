from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board, Topic, Post
from django.contrib.auth.models import User
from .forms import NewTopicForm


# Create your views here.

def home(request):
    # global response_html
    boards = Board.objects.all()
    # boards_names = list()
    # for board in boards:
    #     boards_names.append(board.name)
    #
    #     response_html = '<br>'.join(boards_names)

    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    # or  board=get_object_or_404(Board,id=pk)
    try:
        board = Board.objects.get(id=pk)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, id=pk)
    return render(request, 'new_topic.html', {'board': board})

def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})