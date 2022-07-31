#This is a trainerize API Post script that gets JSON data from the client.  
from genericpath import exists
import json 
import requests 
from types import SimpleNamespace 
import getLoginToken

token = getLoginToken.getToken().seleniumLogin()
print("I ran a new piece of code that gave me: ", token)

headers = {
    'authority': 'api.trainerize.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': token,
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
    'userid': 7660017,
    'startDate': '2022-07-27',
    'endDate': '2022-07-27',
    'unitDistance': 'miles',
    'unitWeight': 'lbs',
}

response = requests.post('https://api.trainerize.com/v03/calendar/getList', headers=headers, json=json_data)

test = json.loads(response.text)
 

 
#Approach: Make a loop statement that looks at the current data. If calories exist, run the nutritionData function to
#put that data into a variable. If it doesn't exist, skip over the data for that day and iterate to the next data point

#create an if statement that checks for the key variable Calories




#[list] use number
#{dictionary} use label

# print("Date      ", test['calendar'][0]['date'])
# print("Calories: ", test['calendar'][0]['items'][1]['detail']['calories'])
# print("Carbs:    ", test['calendar'][0]['items'][1]['detail']['carbsGrams'])
# print("Protein:  ", test['calendar'][0]['items'][1]['detail']['proteinGrams'])
# print("Fats:     ", test['calendar'][0]['items'][1]['detail']['fatGrams'])



# class nutritionData:
#     def __init__(data, calendar, date, items,  ): 
#         data.date = calendar[0]['date'] 
#         data.Calories = calendar[0]['items'][1]['detail']['calories']
#         data.Carbs = calendar[0]['items'][1]['detail']['carbsGrams']
#         data.Protein = calendar[0]['items'][1]['detail']['proteinGrams']
#         data.Fats = calendar[0]['items'][1]['detail']['fatGrams']
    
#     @classmethod
#     def from_json(cls, dataString):
#         data_dict = json.loads(response.text)
#         return cls(**data_dict)

#     def __repr__(self):
#         return f'<user {self.first'}
        
# data = nutritionData.from_json(response.text)

# x = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
# print (x.calendar.items.deatail.calories)


