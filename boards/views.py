from django.shortcuts import  render,redirect ,get_object_or_404
from django.http import HttpResponse, Http404
from .models import Board,Topic,Post
from django.contrib.auth.models import User



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
def new_topic(request , pk):
    board=get_object_or_404(Board,id=pk)
    return render(request,'new_topic.html',{'board':board})

def new_topic(request, pk):
    board = get_object_or_404(Board,id=pk)

    if request.method == 'POST': # recuperation des donnees
        subject = request.POST['subject']
        message = request.POST['message']

        user = User.objects.first()  # TODO: get the currently logged in user

        topic = Topic.objects.create(
            subject=subject,
            board=board,
            starter=user # ca recupere le nom de celui qui a entree l' information
        )

        post = Post.objects.create(
            message=message,
            topic=topic,
            created_by=user
        )

        return redirect('board_topics', pk=board.pk)  # TODO: redirect to the created topic page

    return render(request, 'new_topic.html', {'board': board})