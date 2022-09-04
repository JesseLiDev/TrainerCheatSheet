from http import client
from datetime import datetime as dt
import sys  , datetime 
sys.path.append(".")
from ..getRequests.getLoginToken import getToken
from ..getRequests.getCurrentClients import clientList as cl
from ..getRequests.getClientData import clientData
from ..getRequests.getFoodTargets import foodTargets
from .decisionLogic.nutritionAvg import foodAvg
from .decisionLogic.clientReport import reportClass


class dataReport:
    def runReport(userName, password):
    #STEP 1: Get Login token

        

        tokenTester = getToken().seleniumLogin(userName, password) 
        token = tokenTester
        print("Token Test Successful: ", token) 



        #STEP 2: Get a list of all clients

        clientList =  cl().getClientList(token) 

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

# Step 6: Convert Data to a list of dictionaries
       
        keyList = ["clientID", "firstName", "lastName", "weight","numOfWorkouts","numOfCardio","numOfNutrition","numOfLowCal","avgCal","avgProtein","avgFat","avgCarb","goalCal","goalProtein","goalFats","goalCarb"]

        n = len(clientList)
        dictData = {}
        clientDict = {} 
        clientNum = 0
        for z in range(0, n, 1): 
            
            if len(clientList[z][4]) != 0:
                
                clientDict = {
                    keyList[0]: clientList[z][0],
                    keyList[1]: clientList[z][1],
                    keyList[2]: clientList[z][2],
                    keyList[3]: clientList[z][3][0],
                    keyList[4]: clientList[z][3][1],
                    keyList[5]: clientList[z][3][2],
                    keyList[6]: clientList[z][4][0],
                    keyList[7]: clientList[z][4][1],
                    keyList[8]: clientList[z][4][2],
                    keyList[9]: clientList[z][4][3],
                    keyList[10]: clientList[z][4][4],
                    keyList[11]: clientList[z][4][5],
                    keyList[12]: clientList[z][5][0],
                    keyList[13]: clientList[z][5][1],
                    keyList[14]: clientList[z][5][2],
                    keyList[15]: clientList[z][5][3],
                    }
            else:
                clientDict = {
                    keyList[0]: clientList[z][0],
                    keyList[1]: clientList[z][1],
                    keyList[2]: clientList[z][2],
                    keyList[3]: clientList[z][3][0],
                    keyList[4]: clientList[z][3][1],
                    keyList[5]: clientList[z][3][2],
                    keyList[6]: 0,
                    keyList[7]: 0,
                    keyList[8]: 0,
                    keyList[9]: 0,
                    keyList[10]: 0,
                    keyList[11]: 0,
                    keyList[12]: clientList[z][5][0],
                    keyList[13]: clientList[z][5][1],
                    keyList[14]: clientList[z][5][2],
                    keyList[15]: clientList[z][5][3]
                    }
            
            dictData.update({clientNum: clientDict})
            clientNum += 1


        return dictData
 