from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import math


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


from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def show_view(request):
    # 获取当前页码数
    num = request.GET.get('num', 1)
    n = int(num)
    # 1.查询stu_student表中的所有数据
    stus = Student.objects.all()  # 获取所有的
    # django 分页
    pager = Paginator(stus, 2)
    # 获取当前页面的数据
    try:
        perpage_data = pager.page(n)
        # 返回第一页的数据
    except PageNotAnInteger:
        perpage_data = pager.page(1)
        # 返回最后一页的数据
    except EmptyPage:
        perpage_data = pager.page(pager.num_pages)
    return render(request, 'show.html', {'show': stus, 'pager': pager, 'perpage_data': perpage_data})


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html', {})
    else:
        # 获取请求参数
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # 查询数据库
        if username and password:
            c = Student.objects.filter(username=username, password=password).count()

        # 判断是否登录成功
        if c == 1:
            return HttpResponse("登录成功")
        return HttpResponse("登录失败")


def index_view(request):
    return render(request, 'index.html', {})


def movie_view(request):
    # movie = Movie.objects.all() 获取所有的
    # 接收请求参数 num
    # 原生分页
    num = request.GET.get('num', 1)
    # 处理分页请求
    movies, n = page(num)
    # 分页
    # 页码 num 每页显示记录数size
    #     1     2   [0:2]
    #     2     2   [2:4]
    #     3     2   [4:6]
    #     4     2   [6:8]
    #     num   size     [((num - 1) * size):(num * size)]
    # 上一页的页码
    pre_page_num = n - 1
    # 下一页的页码
    next_page_num = n + 1
    return render(request, 'movie.html',
                  {'movie': movies, 'pre_page_num': pre_page_num, 'next_page_num': next_page_num})


def page(num, size=2):
    # 接收当前页面码
    num = int(num)
    # 总记录数
    totalRecords = Movie.objects.count()
    # 判断是否越界
    if num < 1:
        num = 1
    totalPages = int(math.ceil(totalRecords * 1.0 / size))
    # 取整
    if num > totalPages:
        num = totalPages
    # 计算出每页显示的记录
    movies = Movie.objects.all()[((num - 1) * size):(num * size)]
    return movies, num

def showsql():
    from django.db import connection
    print (connection.queries[-1]['sql'])

