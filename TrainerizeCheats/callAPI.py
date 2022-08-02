from http import client
import sys  
sys.path.append(".")
from getRequests.getLoginToken import getToken
from getRequests.getCurrentClients import clientList
from getRequests.getClientData import clientData
from getRequests.getFoodTargets import foodTargets
from decisionLogic.nutritionAvg import foodAvg

#STEP 1: Get Login token

# token = getToken().seleniumLogin() 
 
# print("I ran a new piece of code that gave me: ", token)


#STEP 2: Get a list of all clients

clientList =  clientList().getClientList() 
 
print("I ran a new piece of code that gave me: ", clientList)
 

#STEP 3: Use clientID to pull Cardio, workout, and nutrition data
#        *Dependent on clientList*

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  clientData().getClientData(clientList[a][0]) 
    clientList[a].append(clientStorage[0])
    clientList[a].append(clientStorage[1])
    a += 1 
 

#STEP 4: Grab Nutrition Targets for every client
#        *Dependent on Step 2 and Step 3*
a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  foodTargets().getFoodTargets(clientList[a][0]) 
    clientList[a].insert(4, clientStorage) 
    a += 1
# print("Test: ", clientList)
 

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
