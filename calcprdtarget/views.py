from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def score(request):
    es_target = int(request.POST["estarget"])
    ac_target = int(request.POST["actarget"])

    res = ac_target * 100 / es_target
    return render(request, 'result.html', {"result": res})