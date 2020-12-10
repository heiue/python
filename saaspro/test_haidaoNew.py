# coding=utf-8
from config import setting
import requests
import json

api = setting.get('api').get('haidaoNew').get('dev')
print(api)

def videoSubject_subjectDataList():
    param = {
        "page": 1,
        "pageSize": 10
    }
    try:
        result = requests.get('%s/videoSubject/subjectDataList' % api, param)
        result = json.loads(result.text)
    except Warning as w:
        print('[warning]'+w.message)
    except Exception as e:
        print('[exception]'+e.message)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=4))

def yiluTemplateVideo_list():
    """
    模版库视频列表
    :return:
    """
    param = {
        "page": 1,
        "garageVideo": 1,
    }
    try:
        result = requests.get('%s/yiluTemplateVideo/list' % api, param)
        result = json.loads(result.text)
    except Warning as w:
        print('[warning]' + w.message)
    except Exception as e:
        print('[exception]' + e.message)
    else:
        print(json.dumps(result, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    # videoSubject_subjectDataList()
    yiluTemplateVideo_list()