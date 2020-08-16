import requests
import json

from pprint import pprint


access_token="62e09f53c9cd334a3e8adc490c49fdcf9632f27a14650701527e2deb7d5b81d0261d6546521672f8bd368"

# response = requests.get(f"https://api.vk.com/method/users.get?user_ids=13718799&access_token={access_token}&v=5.103")
# response = requests.get(f"https://api.vk.com/method/users.get?params[user_ids]=13718799&params[fields]=photo_50%2Ccity%2Cverified&params[name_case]=Nom&params[v]&access_token={access_token}&v=5.103")



# users.get?params[user_ids]=13718799&params[fields]=photo_50%2Ccity%2Cverified&params[name_case]=Nom&params[v]=5.103

# url = 'https://api.vk.com/method/users.get'
# response = requests.get(url, params={'user_ids': 1, 'access_token': access_token, 'v': 5.013})

# response = requests.get(url, params={
#     'user_ids': '13718799',
#     'fields': 'about, activities, city, country, career',
#     'access_token': access_token,
#     'v': 5.013
# })
#
# pprint(response)
# pprint(response.text)
# pprint(response.json())
# print(type(response.json()))

# check users subscriptions

url = 'https://api.vk.com/method/users.getSubscriptions'

response = requests.get(url, params={
    'user_id': '13718799',
    'extended': 1,
    'count': 10,
    'fields': 'name',
    'access_token': access_token,
    'v': 5.013
})

# pprint(response)
# pprint(response.text)
pprint(response.json())

#check friends online

# url = 'https://api.vk.com/method/friends.getOnline'
#
# response = requests.get(url, params={
#     'user_id': '13718799',
#     'count': 10,
#     'order': 'random',
#     'access_token': access_token
#     'v': 5.013
# })
#
# # pprint(response)
# # pprint(response.text)
# pprint(response.json())




# my_response = '''{'response': [{'about': 'у меня все хорошо!',
#                'activities': '',
#                'career': [{'city_id': 314,
#                            'company': 'Gorillagroup',
#                            'country_id': 2,
#                            'position': 'QA Engineer'}],
#                'city': {'id': 314, 'title': 'Киев'},
#                'country': {'id': 2, 'title': 'Украина'},
#                'first_name': 'Ирина',
#                'id': 13718799,
#                'last_name': 'Маликова'}]}'''
#
# pprint(json.loads(my_response))

# json_string = """
# {
#     "researcher": {
#         "name": "Ford Prefect",
#         "species": "Betelgeusian",
#         "relatives": [
#             {
#                 "name": "Zaphod Beeblebrox",
#                 "species": "Betelgeusian"
#             }
#         ]
#     }
# }
# """
# # data = json.loads(json_string)
# # pprint(json.loads(json_string))
#
# pprint(json_string)