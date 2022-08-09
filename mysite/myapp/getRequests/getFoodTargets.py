import requests
import json

class foodTargets:

    def getFoodTargets(self, clientId, token):
        headers = {
            'authority': 'api.trainerize.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': token,
            # Already added when you pass json=
            # 'content-type': 'application/json',
            'datetoday': '2022-08-01 18:42:45',
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
            'userID': clientId,
            'achieved': False,
            'unitWeight': 'lbs',
            'start': 0,
            'count': 20,
        }

        response = requests.post('https://api.trainerize.com/v03/goal/getList', headers=headers, json=json_data)
        

        nutritionData = json.loads(response.text)

        nutritionTargets = []

        if nutritionData:

            
            a = nutritionData['goals'][0]['caloricGoal']
            b = nutritionData['goals'][0]['proteinGrams']
            c = nutritionData['goals'][0]['fatGrams']
            d = nutritionData['goals'][0]['carbsGrams']
            
            nutritionTargets.extend( [a, b, c, d] )
        return(nutritionTargets)

 