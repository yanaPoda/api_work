import random

from config import TOKEN
import requests
import json

base_url=f'https://superheroapi.com/api/{TOKEN}/'
# hero_id='550'
#
# URL=base_url+hero_id
# response=requests.get(URL)
# print(URL)
# print(response.text)
# response2=response.json()
# print(response2)
# print(response2['name'])
# print(response2['powerstats']['speed'])

# for u in range(5):
#     random_id=random.randint(1,700)
#     url1 = f'{base_url}/{random_id}'
#     try:
#         response = requests.get(url1)
#         if response.status_code == 200:
#             data = response.json()
#             with open(f'heroes/{data["name"]}.json',"w") as file:
#                 json.dump(data,file, indent=4, ensure_ascii=False)
#                 print(f'герой {random_id} успешно записан')
#         else:
#             print(f"Ошибка: статус {response.status_code} для id={random_id}")
#
#     except requests.exceptions.RequestException as e:
#         print(f"Ошибка запроса для id={random_id}: {e}")
#     except json.JSONDecodeError as e:
#         print(f"Не удалось декодировать JSON для id={random_id}: {e}")


def read_json(file:str):
    with open(file,'r') as my_file:
        data=json.load(my_file)
        return data




result=read_json('heroes/T-1000.json')
print(result)
