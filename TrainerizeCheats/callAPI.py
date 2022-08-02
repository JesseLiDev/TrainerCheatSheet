from http import client
import datetime  
from datetime import datetime as dt
import sys  
sys.path.append(".")
from getRequests.getLoginToken import getToken
from getRequests.getCurrentClients import clientList
from getRequests.getClientData import clientData
from getRequests.getFoodTargets import foodTargets
from decisionLogic.nutritionAvg import foodAvg

#STEP 1: Get Login token

# tokenTester = getToken().seleniumLogin() 
# token = tokenTester
#print("Token Test Successful: ", token)

token = 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOjcwMTI3NTcsInNjb3BlIjoiQWxsIiwiaWF0IjoxNjU5NDQ4MzUyNjczLCJleHAiOjE2NTk0NzcxNTI2NzN9.1en9omD2uP0vz0f9RlA84K9Fg2b47WFE6-5VP2wqO3w'



#STEP 2: Get a list of all clients

clientList =  clientList().getClientList(token) 
 
print("Get Client List Successful: ", clientList)
 

#STEP 3: Use clientID to pull Cardio, workout, and nutrition data
#        *Dependent on clientList*
#        *Get every day of food since previous Monday
strToday = datetime.date.today().strftime("%Y-%m-%d") #returns a string
dateToday = dt.strptime(strToday,'%Y-%m-%d')
 
if dateToday.weekday() != 0:
    lastMonday = dateToday - datetime.timedelta(days=dateToday.weekday())
    lastMonday = lastMonday.strftime("%Y-%m-%d") 
else:
    lastMonday = dateToday - datetime.timedelta(7)
    lastMonday = lastMonday.strftime("%Y-%m-%d") 

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  clientData().getClientData(clientList[a][0], token, strToday, lastMonday) 
    clientList[a].append(clientStorage[0])
    clientList[a].append(clientStorage[1])
    a += 1 
 
print("Get Client Data Successful: ")

#STEP 4: Grab Nutrition Targets for every client
#        *Dependent on Step 2 and Step 3*
a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  foodTargets().getFoodTargets(clientList[a][0], token) 
    clientList[a].insert(4, clientStorage) 
    a += 1
print("Test: ", clientList)
 

#STEP 5: Create Decision Making Data
#        ~Data Structure at this point~
#        ID-First-Last
#        [Bodyweight, # of workout sessions this week, # of cardio ]
#        [Number of tracked days, Number of Low Calorie Days, Avg Cals, Avg Protein, Avg Fats, Avg Carbs] <- Data from the last 7 days
#        [Goal Calories, Goal Protein, Goal Fats, Goal Carbs ]
#        [All nutrition data by date, cals, protein, fats, carbs...]


a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  foodAvg().foodCalc(clientList[a][5]) 
    clientList[a].insert(4, clientStorage) 
    a += 1
print("Test: ", clientList)


#STEP 6: Print out user summary


