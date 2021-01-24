from django.shortcuts import render

# Create your views here.
from .models import T1
from django.db.models import Avg
from django.http import HttpResponse


def books_short(request):
    # 从models取数据传给template
    shorts = T1.objects.all()
    # 评论数量
    counter = T1.objects.all().count()

    # 平均星级
    star_avg=f"{T1.objects.aggregate(Avg('n_star'))['n_star__avg']:0.1f}"

    # 情感倾向
    sent_avt=f"{T1.objects.aggregate(Avg('sentiment'))['sentiment__avg']:0.2f}"

    # 正向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__gte':0.5}  # 大于
    plus = queryset.filter(**condtions).count() # 字典的形式

    # 负向数量
    queryset = T1.objects.values('sentiment')
    condtions = {'sentiment__lt':0.5}   # 小于
    minus = queryset.filter(**condtions).count()

    return render(request, 'result.html', locals())
    # return HttpResponse(f'平均星际：{star_avg},\
    #                     情感倾向:{sent_avt},\
    #                     正向数量:{plus},\
    #                     负向数量:{minus}')