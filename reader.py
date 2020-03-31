import vk_api
import requests
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


Lonin = input('Login: ')
Password = input('Password: ')
Vk_token = input('Vk_token: ')

session = requests.Session()
vk_session = vk_api.VkApi(Lonin, Password)
vk_session.auth(token_only=False)
vk_session = vk_api.VkApi(token=Vk_token)



longpoll = VkLongPoll(vk_session)

vk = vk_session.get_api()

print('Программа начала работать.')
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

        print(event.type)

        # получаем данные о пользователе
        user_data = vk.users.get(user_ids = event.user_id)
        UserID = user_data[0]["id"]
        UserFirstName = user_data[0]["first_name"]
        UserLastName = user_data[0]["last_name"]

        print('\n------------')
        print(f'Новое сообщеие, \nНаписал: {UserFirstName} {UserLastName}, \nЕго id {UserID}, \nТекст сообщения: {event.text}')
        print('------------')

    if event.type == VkEventType.MESSAGE_EDIT:
        print('Редактирование сообщения')
        print('\n------------')
        print(f'{UserFirstName} {UserLastName} ({UserID}) \nОтредактировал сообщеие, \nТекст сообщения: {event.message}')
        print('------------')
