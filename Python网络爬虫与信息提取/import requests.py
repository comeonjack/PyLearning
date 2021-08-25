import requests
r = requests.get("http://www.sz-hiragawa.com")
print(r.status_code)

print(type(r))

print(r.encoding)

print(r.text)

r.encoding = "utf-8"

print(r.text)