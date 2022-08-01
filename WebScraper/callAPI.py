from http import client
import getLoginToken
import getCurrentClients
import getClientData

#Get Login token
# token = getLoginToken.getToken().seleniumLogin() 
# print("I ran a new piece of code that gave me: ", token)


 #get Current Clients
 
clientList = getCurrentClients.clientList().getClientList() 
# print("I ran a new piece of code that gave me: ", clientList)
 

#Pass each client in client list to


a = 0
for x in clientList:
    clientData =[] 
    clientData = getClientData.clientData().getClientData(clientList[a][0]) 
    clientList[a].append(clientData)
    a += 1
print("Test: ", clientList)