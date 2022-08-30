# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# from .forms import trainerLoginForm

# def index(request):
#     return HttpResponse("Hello World")

# def loginPage(request): 

# #if
#     form = trainerLoginForm(request.POST)
#     if request.method == 'POST':
#         print(request.POST)
#         form = trainerLoginForm(request.POST)
#         if form.is_valid():
#             form.save()
#     context = {'form': form}
#     return render(request, 'login.html', context)
#     # return render(request, 'login.html')
####
import json
from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from .forms import trainerLoginForm 
from .TrainerizeCheats import dataReport
def index(request):
    return HttpResponse("Hello World")
 

def loginPage(request): 

#if the user goes to \loginPage and submits information from the submit button, print 
    
    form = trainerLoginForm() 
    if request.method == 'POST':
        print(request.POST)

        a = dict(request.POST) 
        # z = dataReport.runReport(a["trainerUserName"],a["trainerPassword"])
        
        #Full Example
        f = {0: {'clientID': 7660017, 'firstName': 'Beth', 'lastName': 'Harden', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 1, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 1075.86, 'avgProtein': 76.43, 'avgFat': 40.8, 'avgCarb': 95.17, 'goalCal': 1051.0, 'goalProtein': 110.0, 'goalFats': 39.0, 'goalCarb': 66.0}, 1: {'clientID': 7397039, 'firstName': 'Christie', 'lastName': 'Morelli', 'weight': '151 lbs', 'numOfWorkouts': 1, 'numOfCardio': 1, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 1052.71, 'avgProtein': 50.81, 'avgFat': 56.83, 'avgCarb': 75.65, 'goalCal': 1100.0, 'goalProtein': 98.0, 'goalFats': 40.0, 'goalCarb': 87.0}, 2: {'clientID': 7549163, 'firstName': 'Colleen', 'lastName': 'Rear', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 1, 'avgCal': 200.0, 'avgProtein': 4.0, 'avgFat': 9.0, 'avgCarb': 25.0, 'goalCal': 1151.0, 'goalProtein': 123.0, 'goalFats': 43.0, 'goalCarb': 68.0}, 3: {'clientID': 7663743, 'firstName': 'Colleen', 'lastName': 'Sullivan', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1200.0, 'goalProtein': 114.0, 'goalFats': 44.0, 'goalCarb': 87.0}, 4: {'clientID': 8148365, 'firstName': 'Dawn', 'lastName': 'King', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1378.0, 'goalProtein': 108.0, 'goalFats': 46.0, 'goalCarb': 133.0}, 5: {'clientID': 8277823, 'firstName': 'Gabby', 'lastName': 'Rosenthal', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 1458.02, 'avgProtein': 123.79, 'avgFat': 38.57, 'avgCarb': 149.82, 'goalCal': 1398.0, 'goalProtein': 127.0, 'goalFats': 50.0, 'goalCarb': 110.0}, 6: {'clientID': 7397051, 'firstName': 'Jack', 'lastName': 'Morelli', 'weight': '171.6 lbs', 'numOfWorkouts': 1, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 910.0, 'avgProtein': 36.0, 'avgFat': 32.5, 'avgCarb': 118.0, 'goalCal': 1150.0, 'goalProtein': 121.0, 'goalFats': 42.0, 'goalCarb': 71.0}, 7: {'clientID': 8161311, 'firstName': 'Jaclyn', 'lastName': 'Halcrow', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1802.0, 'goalProtein': 134.0, 'goalFats': 66.0, 'goalCarb': 168.0}, 8: {'clientID': 8260612, 'firstName': 'Jana', 'lastName': 'Tabor', 'weight': '231.4 lbs / 55.5% BF', 'numOfWorkouts': 2, 'numOfCardio': 2, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 1410.0, 'avgProtein': 99.1, 'avgFat': 52.75, 'avgCarb': 151.2, 'goalCal': 1752.0, 'goalProtein': 122.0, 'goalFats': 64.0, 'goalCarb': 172.0}, 9: {'clientID': 7342532, 'firstName': 'Jennifer', 'lastName': 'Smith', 'weight': '138.2 lbs', 'numOfWorkouts': 1, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 945.0, 'avgProtein': 108.5, 'avgFat': 31.53, 'avgCarb': 26.35, 'goalCal': 1026.0, 'goalProtein': 100.0, 'goalFats': 38.0, 'goalCarb': 71.0}, 10: {'clientID': 8394913, 'firstName': 'Jennifer', 'lastName': 'Solis', 'weight': '196.6 lbs', 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 925.29, 'avgProtein': 60.02, 'avgFat': 67.49, 'avgCarb': 24.23, 'goalCal': 1300.0, 'goalProtein': 111.0, 'goalFats': 43.0, 'goalCarb': 117.0}, 11: {'clientID': 7365712, 'firstName': 'Leann', 'lastName': 'Klenda', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 1, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1374.0, 'goalProtein': 126.0, 'goalFats': 50.0, 'goalCarb': 105.0}, 12: {'clientID': 7331237, 'firstName': 'Pam', 'lastName': 'Horton', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1100.0, 'goalProtein': 133.0, 'goalFats': 40.0, 'goalCarb': 52.0}, 13: {'clientID': 7271566, 'firstName': 'Patricia', 'lastName': 'LeBlanc', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1203.0, 'goalProtein': 104.0, 'goalFats': 47.0, 'goalCarb': 91.0}, 14: {'clientID': 7647326, 'firstName': 'Sarah', 'lastName': 'Quinn', 'weight': '156 lbs', 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1349.0, 'goalProtein': 137.0, 'goalFats': 45.0, 'goalCarb': 99.0}, 15: {'clientID': 8401809, 'firstName': 'Stephanie', 'lastName': 'Devik', 'weight': '260.8 lbs', 'numOfWorkouts': 1, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 835.0, 'avgProtein': 25.0, 'avgFat': 22.4, 'avgCarb': 126.5, 'goalCal': 1100.0, 'goalProtein': 105.0, 'goalFats': 40.0, 'goalCarb': 80.0}, 16: {'clientID': 8232485, 'firstName': 'Tara', 'lastName': 'Miller', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 0, 'numOfLowCal': 0, 'avgCal': 0, 'avgProtein': 0, 'avgFat': 0, 'avgCarb': 0, 'goalCal': 1349.0, 'goalProtein': 119.0, 'goalFats': 45.0, 'goalCarb': 117.0}, 17: {'clientID': 7571188, 'firstName': 'Tina', 'lastName': 'Phillips', 'weight': 0, 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 1, 'avgCal': 380.0, 'avgProtein': 22.0, 'avgFat': 14.0, 'avgCarb': 50.0, 'goalCal': 1200.0, 'goalProtein': 101.0, 'goalFats': 47.0, 'goalCarb': 94.0}, 18: {'clientID': 7671940, 'firstName': 'Tricia', 'lastName': 'Biever', 'weight': '310 lbs', 'numOfWorkouts': 0, 'numOfCardio': 0, 'numOfNutrition': 1, 'numOfLowCal': 0, 'avgCal': 720.54, 'avgProtein': 37.9, 'avgFat': 28.0, 'avgCarb': 50.0, 'goalCal': 1200.0, 'goalProtein': 124.0, 'goalFats': 44.0, 'goalCarb': 77.0}}        
 
        z = {'json_list': f}
 
        print(z)
        return render(request, 'output.html', z) 
        # if form.is_valid():
        #     form.save()
    context = {'form': form}
    return render(request, 'login.html', context)

