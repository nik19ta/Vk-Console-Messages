import vk_api
import requests


Lonin = input('Login: ')
Password = input('Password: ')
Vk_token = input('Vk_token: ')



session = requests.Session()
vk_session = vk_api.VkApi(Lonin, Password)
vk_session.auth(token_only=False)
vk_session = vk_api.VkApi(token=Vk_token)

vk = vk_session.get_api()

options = {
1:'1: Удалить человека из беседы',
2:'2: Добавить человека в беседу',
3:'3: Поменять название беседы',
4:'4: Получить информацию о чате',
5:'5: Получить информацию о беседах',
6:'6: Получить историю сообщений'
}

print('-------------------')
print('Выберете действие: ')
print(options[1])
print(options[2])
print(options[3])
print(options[4])
print(options[5])
print(options[6])
print('-------------------')

option = int(input('Действие: '))


if option == 1:
    chat_id = input('chat_id: ')
    user_id = input('user_id: ')

    vk.messages.removeChatUser(
    chat_id = chat_id,
    user_id = user_id
    )
elif option == 2:
    chat_id = input('chat_id: ')
    user_id = input('user_id: ')

    vk.messages.addChatUser(
    chat_id = chat_id,
    user_id = user_id
    )
elif option == 3:
    chat_id = input('chat_id: ')

    vk.messages.editChat(
    chat_id = chat_id,
    title = input('Новое название беседы: ')
    )
elif option == 4:
    chat_id = input('chat_id: ')
    infochat = vk.messages.getChat(chat_id = chat_id)
    print('-------------------')
    print('Тип:',infochat['type'])
    print('Название беседы:',infochat['title'])
    print('Admin:',infochat['admin_id'])
    print('Количество пользователей:',infochat['members_count'])
    print('Пользователи:',infochat['users'])
    print('Id чата:',infochat['id'])
    print('-------------------')
elif option == 5:
    chats = vk.messages.getConversations()
    print(chats['items'])
elif option == 6:
    messages = vk.messages.getHistory(
    count=200,
    user_id=user_id
    )
    print(messages)
