import requests, json

class clientList:

    def getClientList(self):
        headers = {
            'authority': 'api.trainerize.com',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySUQiOjcwMTI3NTcsInNjb3BlIjoiQWxsIiwiaWF0IjoxNjU5Mzk4MzU0NzA0LCJleHAiOjE2NTk0MjcxNTQ3MDR9.QPUG0ksKe_-qiYamA_dRzTymbLAHVdPgx_uYb9-8nl0',
            'content-type': 'application/json; charset=UTF-8',
            'datetoday': '2022-07-31 14:02:44',
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
            'view': 'activeClient',
            'sort': 'name',
            'start': 0,
            'count': 20,
            'includeBasicMember': False,
            'verbose': True,
            'filter': {},
            'userID': 7012757,
        }

        response = requests.post('https://api.trainerize.com/v03/user/getClientList', headers=headers, json=json_data)

        test = json.loads(response.text)

        a = 0 
        client = []
        clientList = []
        for x in test['users']:

            client.append(test['users'][a]['id'])
            client.append(test['users'][a]['firstName'])
            client.append(test['users'][a]['lastName'])
            clientList.append(client) 
            client = []
            a += 1
        return(clientList)
         

