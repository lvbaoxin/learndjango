from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def index_view(request):
    m = request.method
    if m == 'GET':
        return render(request, 'register.html', {})
    else:
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username and password:
            # 创建模型对象
            stu = Student(username=username, password=password)
            stu.save()
            return HttpResponse("注册成功")
        return HttpResponse("注册失败")
