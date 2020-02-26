from django.shortcuts import render
from app01 import models
from utils.pager import PageInfo


def custom(request):
    all_count = models.UserInfo.objects.all().count()
    page_info = PageInfo(request.GET.get('page'), all_count, 20, '/custom.html', 11)
    user_list = models.UserInfo.objects.all()[page_info.start():page_info.end()]
    return render(request, 'custom.html', {'user_list': user_list, 'page_info': page_info})


def index(request):
    # for i in range(100):
    #     name = 'user'+str(i)
    #     models.UserInfo.objects.create(name=name, age=18, ut_id=1)

    user_list = models.UserInfo.objects.all()
    return render(request, 'index.html', {'user_list': user_list})
