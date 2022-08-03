from django.http import HttpResponse
from django.shortcuts import render
from.models import place
from.models import team
# Create your views here.
def fun (request):
    obj=place.objects.all()
    obj1 = team.objects.all()
    return render(request ,"index.html",{'result':obj,'result1':obj1})



# def addition(request):
#     x=int(request.GET['no1'])
#     y = int(request.GET['no2'])
#     res=x+y
#     return render (request,'new2.html',{'result':res})
# def fun1 (request):
#     return render (request,"new2.html")
# def fun2 (request):
#     return HttpResponse("hello i am bc")