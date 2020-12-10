import requests
from config import setting
import json
import io
from os.path import *
import time

api = setting.get('api').get('saas').get('dev')
version = setting.get('version')


def decodeCrypt(data):
    result = requests.post(api + '/cyEnDe/decode?version=' + version, data)
    return json.loads(result.text)


def encodeCrypt(data):
    result = requests.post(api + '/cyEnDe/encode?version=' + version, data)
    print('encode:' + result.text)
    return json.loads(result.text)


def login():
    param = {
        "name": "18811111111",
        "pwd": "zxcvbnm",
        "version": version
    }
    data = encodeCrypt(param)
    result = requests.post(api + '/login/login', data)
    data = json.loads(result.text)
    result = decodeCrypt(data)
    return result


def getU():
    f = io.open(dirname(abspath(__file__)) + '/login.txt', 'r', encoding='utf-8')
    read = f.read()
    f.close()
    if read != '' and json.loads(read).get('expired') > int(time.time()):
        read = json.loads(read)
        U = read.get('U')
    else:
        reuslt = login()
        if reuslt.get('error') != 0:
            return False
        U = reuslt.get('U')
        reuslt['expired'] = int(time.time()) + 43200
        reuslt = json.dumps(reuslt, ensure_ascii=False)
        f_w = io.open(dirname(abspath(__file__)) + '/login.txt', 'w', encoding='utf-8')
        f_w.write(reuslt)
        f_w.close()
    return U


def getParam(data, crypt=True):
    U = getU()
    data["version"] = version
    data["U"] = U
    data["device"] = 2
    data["appversion"] = 51
    print(data)
    if crypt:
        result = encodeCrypt(data)
    else:
        result = data
    return result


if __name__ == '__main__':
    print dirname(abspath(__file__))
