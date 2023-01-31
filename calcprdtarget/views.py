from django.shortcuts import render
from django.http import HttpResponse
from calcprdtarget.models import prdanalysis 


# Create your views here.

def home(request):
    display_data = prdanalysis.objects.all()
    data = {
        "displayData": display_data
    }
    try:
        if request.method == "POST":
            estarget = request.POST['estarget']
            actarget = request.POST['actarget']
            score = request.POST['score']
            bonus = request.POST['bonus']
            date = request.POST['date']
            time = request.POST['time']
            prdanalysis_m = prdanalysis(es_target=estarget, ac_target=actarget, score=score, bonus=bonus,date=date, time=time )
            prdanalysis_m.save()
    except:
        pass
    return render(request, 'home.html', data)
