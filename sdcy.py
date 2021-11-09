import requests
from datetime import datetime
import time


url = 'https://login.rz.ruhr-uni-bochum.de/cgi-bin/laklogin'
def login():
    user_agent_val = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'
    session = requests.Session()
    r = session.get(url, headers={'User-Agent': user_agent_val})
    session.headers.update({'Referer': url})
    session.headers.update({'User-Agent': user_agent_val})
    post_request = session.post(url, {
        'code' : 1,
        'loginid' : 'login',
        'password' : 'password',
        'ipaddr' : 'ip',
        'action' : 'Login'
        })
while(True):
    login()
    print('Logged at:',datetime.now().time())
    time.sleep(60*60)
