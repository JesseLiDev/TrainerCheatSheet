import getLoginToken
import getCurrentClients

#Get Login token
# token = getLoginToken.getToken().seleniumLogin() 
# print("I ran a new piece of code that gave me: ", token)


 #get Current Clients
 
clientList = getCurrentClients.client().getClientList() 
print("I ran a new piece of code that gave me: ", clientList)



