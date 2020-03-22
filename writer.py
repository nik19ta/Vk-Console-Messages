import vk_api
import requests
from vk_api.utils import get_random_id


Lonin = input('Login')
Password = input('Password')
Vk_token = input('Vk_token')


session = requests.Session()
vk_session = vk_api.VkApi(Lonin, Password)
vk_session.auth(token_only=False)
vk_session = vk_api.VkApi(token=Vk_token)


vk = vk_session.get_api()

print('\n------------')
print('Программа начала работать')
print('Что бы отправить сообщение через запятую напиши')
print('\n------------')

while True:
    data = input("Отправить сообщение: ")

    try:
        user_id = data.split(',')[0]
        text = data.split(',')[1]

        vk.messages.send( #Отправляем сообщение
        user_id=user_id,
        message=text,
        random_id=get_random_id())

        print('Сообщение отправленно.')
    except:
        print('Отправить не получилось.')
