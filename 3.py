import json
import requests


def avgRotorSpeed(statusQuery, parentId):
    uri = "https://jsonmock.hackerrank.com/api/iot_devices/search?status={}&page={}"
    req = requests.get(uri.format(statusQuery, 0))
    res = json.loads(req.content)
    total_pages = res['total_pages']

    speedTotal = 0
    cnt = 0

    total_data = []
    parent_alias = None
    find = False
    for i in range(1, total_pages + 1):
        req = requests.get(uri.format(statusQuery, i))
        res = json.loads(req.content)
        data = res['data']
        total_data.append(data)
        if not find:
            for datum in data:
                if datum['asset']['id'] == parentId:
                    parent_alias = datum['asset']['alias']
                    find = True
                    break

    for data in total_data:
        for datum in data:
            if datum.get('parent'):
                parent_id = None
                parent_name = None
                if datum['parent'].get('id'):
                    parent_id = datum['parent']['id']
                if datum['parent'].get('alias'):
                    parent_name = datum['parent']['alias']
                if parent_id == parentId or parent_name == parent_alias:
                    cnt += 1
                    speedTotal += datum['operatingParams']['rotorSpeed']
    if cnt:
        return speedTotal // cnt
    return 0


print(avgRotorSpeed("RUNNING", 7))
