import json
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import trainerLoginForm 
from .TrainerCheats import dataReport
def index(request):
    return HttpResponse("Hello World")


def loginPage(request): 
 
    return render(request,"login.html")
 

def loadingPage(request):
    if request.method == 'POST':
    
        username = request.POST['email']
        password = request.POST['password']

        z = dataReport.runReport(username,password) 
        z = {'json_list': z}
        return render(request, 'output.html', z)  


def aboutPage(request): 
    return render(request, 'about.html')