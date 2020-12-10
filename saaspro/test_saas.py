# coding=utf-8
from config import setting
import requests
import saas.saas as saas
import json

setting.set('version', 'v4.9')
api = setting.get('api').get('saas').get('dev')


def carmodel_selectPbrand():
    param = {}
    param = saas.getParam(param)

    try:
        result = requests.post('%s/carmodel/selectPbrand' % api, param)
        result = json.loads(result.text)
        result = saas.decodeCrypt(result)
    except Warning as w:
        print(w.message)
        pass
    except Exception as e:
        print(e.message)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=4))



def carmodel_carModelConfigs():
    """
    车型资料-车型对比
    :return:
    """
    param = {
        "model_ids": "34192,36289"
    }
    param = saas.getParam(param)

    try:
        result = requests.post('%s/carmodel/carModelConfigs' % api, param)
        print(result)
        result = json.loads(result.text)
        result = saas.decodeCrypt(result)
    except Warning as w:
        print(w.message)
        pass
    except Exception as e:
        print(e.message)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=4))

def luck_run():
    """
    抽奖
    :return:
    """
    param = {}
    param = saas.getParam(param)

    try:
        print(api)
        result = requests.post('%s/promotionLuckyDraw/luckDraw' % api, param)
        result = json.loads(result.text)
        result = saas.decodeCrypt(result)
        print(result)
    except Warning as w:
        print(w.message)
        pass
    except Exception as e:
        print(e.message)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=4))

def luck_list():
    param = {}
    param = saas.getParam(param, False)

    try:
        print(api)
        result = requests.post('%s/promotionLuckyDraw/prizeList' % api, param)
        result = json.loads(result.text)
    except Warning as w:
        print(w.message)
        pass
    except Exception as e:
        print(e.message)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    luck_list()