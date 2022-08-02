from http import client
from datetime import datetime as dt
import sys  , datetime 
sys.path.append(".")
from getRequests.getLoginToken import getToken
from getRequests.getCurrentClients import clientList
from getRequests.getClientData import clientData
from getRequests.getFoodTargets import foodTargets
from decisionLogic.nutritionAvg import foodAvg
from decisionLogic.clientReport import reportClass

#STEP 1: Get Login token

# tokenTester = getToken().seleniumLogin() 
# token = tokenTester
#print("Token Test Successful: ", token)

token = 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOjcwMTI3NTcsInNjb3BlIjoiQWxsIiwiaWF0IjoxNjU5NDQ4MzUyNjczLCJleHAiOjE2NTk0NzcxNTI2NzN9.1en9omD2uP0vz0f9RlA84K9Fg2b47WFE6-5VP2wqO3w'



#STEP 2: Get a list of all clients

clientList =  clientList().getClientList(token) 

print("Get Client List Successful \n")


#STEP 3: Use clientID to pull Cardio, workout, and nutrition data

strToday = datetime.date.today().strftime("%Y-%m-%d") #returns a string
dateToday = dt.strptime(strToday,'%Y-%m-%d')
 
if dateToday.weekday() != 0:
    lastMonday = dateToday - datetime.timedelta(days=dateToday.weekday())
    strlastMonday = lastMonday.strftime("%Y-%m-%d") 
else:
    lastMonday = dateToday - datetime.timedelta(7)
    strlastMonday = lastMonday.strftime("%Y-%m-%d") 

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  clientData().getClientData(clientList[a][0], token, strToday, strlastMonday) 
    clientList[a].append(clientStorage[0])
    clientList[a].append(clientStorage[1])
    a += 1 
 
print("Get Client Data Successful \n")


#STEP 4: Grab Nutrition Targets for every client 

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  foodTargets().getFoodTargets(clientList[a][0], token) 
    clientList[a].insert(4, clientStorage) 
    a += 1
print("Get Nutrition Targets Successful \n")
 

#STEP 5: Get Nutrition Average Data

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  foodAvg().foodCalc(clientList[a][5]) 
    clientList[a].insert(4, clientStorage) 
    a += 1
print("Get Nutrition Averages Successful")


#STEP 6: Print out user summary

a=0
for x in clientList:

    runReport = reportClass(clientList[a], dateToday, lastMonday)
    runReport.getGeneralReport()
    a+=1