from http import client
import sys  
sys.path.append(".")
from getRequests.getLoginToken import getToken
from getRequests.getCurrentClients import clientList
from getRequests.getClientData import clientData
from getRequests.getFoodTargets import foodTargets
import time

startTime = time.time()
 

#STEP 1: Get Login token

token = getToken().seleniumLogin() 
t1 = time.time()
p1 = t1 - startTime
print(p1)
# print("I ran a new piece of code that gave me: ", token)


#STEP 2: Get a list of all clients

clientList =  clientList().getClientList() 
t2 = time.time()
p2 = t2 - startTime
print(p2)
# print("I ran a new piece of code that gave me: ", clientList)
 

#STEP 3: Use clientID to pull Cardio, workout, and nutrition data
#        *Dependent on clientList*

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  clientData().getClientData(clientList[a][0]) 
    clientList[a].append(clientStorage[0])
    clientList[a].append(clientStorage[1])
    a += 1 

t3 = time.time()
p3 = t3 - startTime
print(p3)
#STEP 4: Grab Nutrition Targets for every client

a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  foodTargets().getFoodTargets(clientList[a][0]) 
    clientList[a].insert(4, clientStorage) 
    a += 1
print("Test: ", clientList)

t4 = time.time()
p4 = t4 - startTime
print(p4)

#STEP 5:
