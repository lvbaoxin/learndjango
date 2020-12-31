from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def register_view(request):
    m = request.method
    if m == 'GET':
        return render(request, 'register.html', {})
    else:
        # 获取请求参数
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username and password:
            # 创建模型对象
            stu = Student(username=username, password=password)
            # 插入数据库
            stu.save()
            return HttpResponse("注册成功")
        return HttpResponse("注册失败")


def show_view(request):
    # 1.查询stu_student表中的所有数据
    stus = Student.objects.all()

    return render(request, 'show.html', {'show': stus})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        # 获取请求参数
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # 查询数据库
        if username and password:
            c = Student.objects.filter(username = username, password = password).count()

        # 判断是否登录成功
        if c == 1:
            return HttpResponse("登录成功")
        return HttpResponse("登录失败")


def index_view(request):
    return render(request, 'index.html', {})


def movie_view(request):
    movie = Movie.objects.all()


    return render(request, 'movie.html', {'movie': movie})
