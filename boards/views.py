from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Board


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


def board_topics(request, id_board):
    try:
        board = Board.objects.get(id=id_board)
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'topics.html', {'board': board})
