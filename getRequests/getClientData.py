#This is a trainerize API Post script that gets JSON data from the client.  
#This Document is for testing purposes. Requirements:
#You must pass in the authorization code in order for this code to work
  
import json 
import requests  
import datetime  

today = datetime.date.today()
lastMonday = today - datetime.timedelta(days=today.weekday())
 
today = datetime.date.today().strftime("%Y-%m-%d")
lastMonday = lastMonday.strftime("%Y-%m-%d")
 
class clientData:

    def getClientData(self, clientId):        
        headers = {
            'authority': 'api.trainerize.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOjcwMTI3NTcsInNjb3BlIjoiQWxsIiwiaWF0IjoxNjU5MjkwMjYzMDcxLCJleHAiOjE2NTkzMTkwNjMwNzF9.jHYtAKbzGalGYwcQB-KEt5oyJMIb2juEjQHQuJRQAPc',
            'content-type': 'application/json; charset=UTF-8',
            'datetoday': '2022-07-28 15:01:33',
            'origin': 'https://justinbauerfitness.trainerize.com',
            'referer': 'https://justinbauerfitness.trainerize.com/',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'tr-from': 'web',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        } 
        json_data = {
            'userid': clientId, #clientID,
            'startDate': lastMonday,
            'endDate': today,
            'unitDistance': 'miles',
            'unitWeight': 'lbs',
        }

        response = requests.post('https://api.trainerize.com/v03/calendar/getList', headers=headers, json=json_data)

        clientData = json.loads(response.text)

        if clientData:
            allClientData = []
            countA = 0
            countB = 0
            weekAvgCount = 0
            weekAvgTotal = 0
            for date in clientData['calendar']:
                try: 
                    aa = clientData['calendar'][countA]['date']
                            
                    for items in clientData['calendar'][countA]["items"]:
                        try:
                            a = clientData['calendar'][countA]['items'][countB]['detail']['calories']
                            b = clientData['calendar'][countA]['items'][countB]['detail']['proteinGrams']
                            c = clientData['calendar'][countA]['items'][countB]['detail']['fatGrams']
                            d = clientData['calendar'][countA]['items'][countB]['detail']['carbsGrams']
                            
                            allClientData.extend([aa,a,b,c,d])
                            # print("Date: ", aa)
                            # print("Calories: ", a)
                            # print("Protein: ", b)
                            # print("Fats: ", c)
                            # print("Carbs: ", d)
                            # print("\n" )
                            countB += 1
                            weekAvgCount +=1
                            weekAvgTotal +=a
                        except:
                            countB += 1
                    countA +=1
                    countB = 0
                except:
                    countA +=1
                    countB = 0
        else:
            print("List is empty")

        if(weekAvgCount != 0 and weekAvgTotal != 0):
            caloireSummary = weekAvgTotal/weekAvgCount
            
            allClientData.insert(0, weekAvgCount)
            allClientData.insert(0, caloireSummary)
        else:
            allClientData.insert(0, 0)
            allClientData.insert(0, 0)
        return allClientData
 

