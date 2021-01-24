from django.shortcuts import render

# Create your views here.

from .models import Ironmanorm
from django.db.models import Avg
from django.http import HttpResponse

def comment(request):
    # 从models取数据传给template
    com_all = Ironmanorm.objects.all()
    condtions = {'starts__gte':4}  # 大于等于
    comment = com_all.filter(**condtions) # 字典的形式

    # return HttpResponse('123')
    return render(request, 'index.html', locals())