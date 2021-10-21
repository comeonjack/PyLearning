import requests

try:
    kv = {'wd': 'Python'}
    h = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get("http://www.baidu.com/s", params = kv,headers = h)
    r.raise_for_status()
    print(r.raise_for_status())
    print(r.request.url)
    print(len(r.text))
except:
    print("爬取失败")
