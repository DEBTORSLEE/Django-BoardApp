from django.shortcuts import render,get_object_or_404,redirect

# Create your views here.
from board.models import Board
from django.views.decorators.csrf import csrf_exempt

def index(request):
    board_list = Board.objects.all().order_by('-wdate')[:5]
    context = {'board_list':board_list}
    return render(request,'board/index.html',context)
    
@csrf_exempt
def new(request):
    if request.method == "POST":
        subj =request.POST.get('subj')
        cont = request.POST.get('cont')
        board = Board(subj=subj,cont=cont)
        board.save()
        return redirect("/board")
    
    else:
        return render(request,'board/new.html')
    
def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    
    i = board.hit + 1
    board.hit = i
    
    context = {'board':board}
    return render(request,'board/detail.html',{'board':board})
    
def delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect("/board")
    
@csrf_exempt
def edit(request,board_id):
    board = get_object_or_404(Board, pk=request.POST['board_id'])
    context = {'board':board}
    return render(request,'board/edit.html',{'board':board})
    
@csrf_exempt
def update(request,board_id):
    board = Board.objects.get(pk=board_id)
    board.subj = request.POST.get('subj')
    board.cont = request.POST.get('cont')
    board.save()
    
    return redirect("/board")