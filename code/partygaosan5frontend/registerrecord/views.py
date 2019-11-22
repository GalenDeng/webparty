from urllib import request, parse

try:
    import json
except ImportError:
    import simplejson as json
from django.shortcuts import render
from urllib.parse import urljoin

# Create your views here.

PAGESIZE = 5

# 引入API
partyname_url = 'http://127.0.0.1:8077/name/'

# 读取api数据
def getdata(url, data=None):
    # url = r'http://xxx/xxx/xxxx?'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Cookie':'csrftoken = ESRXf1EotrWbE7DQlGfy…n2QeqfyQZTCBWzgPWChU3YjBuRpXz',
    }
    # data = {
    #     'first': 'true',
    #     'pn': 1,
    #     'kd': 'Python'
    #     }
    # urlencode（）主要作用就是将url附上要提交的数据。
    # 经过urlencode（）转换后的data数据为?first=true?pn=1?kd=Python，最后提交的url为
    # http://xxxxx/xx/xx?first=true?pn=1?kd=Python
    try:
        if data:
            # data = parse.urlencode(data).encode('utf8')
            # data 参数如果要传必须传 bytes （字节流）类型的，如果是一个字典，可以先用 urllib.parse.urlencode() 编码。
            # data = bytes(parse.urlencode(data), encoding="utf8")
            data = '?' + parse.urlencode(data)
            # 使用request（）来包装请求，再通过urlopen（）获取页面。
            url = urljoin(url, data)
            req = request.Request(url=url, headers=headers, method='GET')
        else:
            req = request.Request(url=url, headers=headers)

        reponsedata = request.urlopen(req, timeout=10).read()
        reponsedata = reponsedata.decode('utf-8')
        returndata = json.loads(reponsedata)
    except Exception as e:
        print(e)
        returndata = {'result': e, 'code': e, 'msg': '请求api数据错误！', 'data': '{}', 'redirect_url': ''}
    return returndata


# 实现全局变量
def globl_init(request):
    partyname_list = getdata(partyname_url)
    user = request.user
    return locals()


# 实现首页功能
def index(request):
    data = {

    }
    partyname_data = getdata(partyname_url, data)

    user = []
    return render(request, 'index.html', locals())



