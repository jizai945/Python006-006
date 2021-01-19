# index/urls.py
from django.urls import path, re_path, register_converter
from . import views, converters

register_converter(converters.IntConverter, 'myint')
register_converter(converters.FourDigitYearConverter, 'yyyy')

urlpatterns=[
    path('', views.index),

    ### 带变量的URL
    # path('<int:year>', views.year), # 值接受整数，其他类型返回404
    path('<int:year>/<str:name>', views.name),

    ### 正则匹配
    # ?P表示后面是一个变量和他们能够匹配的正则表达式 .html表示匹配网页
    re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),

    ### 自定义过滤器
    # path('<myint:year>', views.myyear),
    path('<yyyy:year>', views.year),
    path('books', views.books),
]

