import vk_api
import requests


from Chat import Chat
from Chat import Chat
from EternalOnline import EternalOnline
from EternalOffline import EternalOffline
from Info import Info
from Reader import Reader
from Writer import Writer

class Main:
    """Конфигурация"""

    def __init__(self,Lonin,Password,Vk_token):
        self.Lonin = Lonin
        self.Password = Password
        self.Vk_token = Vk_token


Config = Main('89646997211','Sekret2807','6b91ae2108d55802d080998f92bcbf2e86752dde82068115c018af24a7b510507a01fa33bf4e84df1510e')

session = requests.Session()
vk_session = vk_api.VkApi(Config.Lonin, Config.Password)
vk_session.auth(token_only=False)
vk_session = vk_api.VkApi(token=Config.Vk_token)


vk = vk_session.get_api()

menu = {
1:'1: Перейти к разделам чата',
2:'2: Получить информацию о аккаунте',
3:'3: Войти в Online',
4:'4: Войти в Offline',
5:'5: Принимать сообщения',
6:'6: Написать сообщение',
}
while True:
    print('-------------------')
    print('Выберете действие: ')
    print(menu[1])
    print(menu[2])
    print(menu[3])
    print(menu[4])
    print(menu[5])
    print(menu[6])
    print('-------------------')

    menuOption = int(input("Выбери действие: "))
    if menuOption == 1:
        try:
            Chat(vk)
        except:
            print('-------------------')
            print('Что то пошло не так')
    if menuOption == 2:
        try:
            Info(vk)
        except:
            print('-------------------')
            print('Что то пошло не так')
    if menuOption == 3:
        try:
            EternalOnline(vk)
        except:
            print('-------------------')
            print('Что то пошло не так')
    if menuOption == 4:
        try:
            EternalOffline(vk)
        except:
            print('-------------------')
            print('Что то пошло не так')
    if menuOption == 5:
        try:
            Reader(vk,vk_session)
        except:
            print('-------------------')
            print('Что то пошло не так')
    if menuOption == 6:
        try:
            Writer(vk)
        except:
            print('-------------------')
            print('Что то пошло не так')
