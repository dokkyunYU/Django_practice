from email import message
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def greeting(request):
    context = {
        'name': 'dq',
        'foods': ['fdfdf', 'qrewqr'],
    }
    return render(request, 'greeting.html', context)


def throw(request):
    context = {'name': 'qq'}
    return render(request, 'throw.html', context)


def catch(request):
    depart = (request.GET.get('depart'),)
    name = (request.GET.get('name'),)
    if depart == '대전 2반':
        if name == '유덕균':
            message = "오셨습니까 주인님"
        else:
            message = "교육생이시군요 반갑습니다"
    context = {'message': message}
    return render(request, 'catch.html', context)
