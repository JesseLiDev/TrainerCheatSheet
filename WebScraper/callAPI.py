import getLoginToken
import getCurrentClients
import getClientData

#Get Login token
# token = getLoginToken.getToken().seleniumLogin() 
# print("I ran a new piece of code that gave me: ", token)


 #get Current Clients
 
# clientList = getCurrentClients.clientList().getClientList() 
# print("I ran a new piece of code that gave me: ", clientList)


#Pass each client in client list to

clientData = getClientData.decisionData().getDecisionData(7660017) 
print("I ran a new piece of code that gave me: ", clientData)