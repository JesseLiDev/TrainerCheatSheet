from http import client
import sys  
sys.path.append(".")
from getRequests.getLoginToken import getToken
from getRequests.getCurrentClients import clientList
from getRequests.getClientData import clientData

#Get Login token
# token = getLoginToken.getToken().seleniumLogin() 
# print("I ran a new piece of code that gave me: ", token)


 #get Current Clients
 
clientList =  clientList().getClientList() 
# print("I ran a new piece of code that gave me: ", clientList)
 

#Pass each client in client list to
#   Dependent on clientList
a = 0
for x in clientList:
    clientStorage =[] 
    clientStorage =  clientData().getClientData(clientList[a][0]) 
    clientList[a].append(clientStorage)
    a += 1
print("Test: ", clientList)

