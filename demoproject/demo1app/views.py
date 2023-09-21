from django.http import HttpResponse
from django.shortcuts import render
from.models import place,person


def form(request):
    obj=place.objects.all()
    obj1=person.objects.all()
    return render(request,"login.html",{'result':obj,'result1':obj1})





















