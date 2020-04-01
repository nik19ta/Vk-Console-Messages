import vk_api
import requests

def Info(vk):
    info = vk.account.getProfileInfo()
    vkinfo = vk.account.getInfo()

    print('-------------------')
    print('Имя:',info['first_name'])
    print('Фамилия:',info['last_name'])
    print('Дата рождения:',info['bdate'])
    print('Город:',info['city']['title'])
    print('Страна:',info['country']['title'])
    print('Родной город:',info['home_town'])
    print('Телефон:',info['phone'])
    print('Короткое имя:',info['screen_name'])
    print('-')
    print('двухфакторная аунтификация',vkinfo['2fa_required'])
    print('Страна',vkinfo['country'])
    print('-------------------')
