import requests, time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=300)
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__main__":
    url = "http://www.sz-hirigawa.com"
    t1 = time.perf_counter()
    for i in range(100):
        getHTMLText(url)
        t2 = time.perf_counter()
    print("爬取100次公司主页，共用时{:.2f}S。".format(t2 - t1))
