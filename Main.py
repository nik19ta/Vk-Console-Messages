from flask import Flask, render_template, request, redirect, url_for, make_response
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


Config = Main('89646997211','!vSNkei.KKcr1oE9mtT','ad02893880d0a9db76154d91da00a045e57494854dea997e90f3c534c1435fcec691d980d47191129c76b')

session = requests.Session()
vk_session = vk_api.VkApi(Config.Lonin, Config.Password)
vk_session.auth(token_only=False)
vk_session = vk_api.VkApi(token=Config.Vk_token)


vk = vk_session.get_api()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print('ok')
    response = make_response('ok', 200)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # return response
    chats = vk.messages.getConversations()
    print(chats['items'])

    data = {'data': chats}

    response = make_response(data, 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/<id>', methods=['GET'])
def Chat(id=None):
    print(id)
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # return response
    chats = vk.messages.getHistory(
    user_id=id,
    offset=50,
    rev=0
    )


    list = {'data': chats}

    print(list)

    return render_template('index.html', chats=list['data']['items'])



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
