from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello Django Timo!")

# path('<int:year>', views.year),
def year(request, year):
    # return HttpResponse(year)
    return redirect('/2020.html')

# path('<int:year>/<str:name>', views.name),
#                   关键字参数
def name(request, **kwargs):
    return HttpResponse(str(kwargs['year'])+kwargs['name'])

# re_path('(?P<year>[0-9]{4}).html', views.myyear, name='urlyear'),
# path('<myint:year>', views.myyear),
def myyear(request, year):
    return render(request, 'yearview.html')    