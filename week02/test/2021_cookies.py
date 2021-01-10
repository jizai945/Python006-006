import requests

# 在同一个Session 实例发出的所有请求之间保持cookie
s = requests.Session()

s.get('htttp://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('htttp://httpbin.org/cookies')

print(r.text)

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('htttp://httpbin.org/cookies/set/sessioncookie/123456789')