# http 协议的GET方法
import requests
r = requests.get('https://github.com')
r.status_code
r.headers['content-type']

# r.text
r.encoding
# r.json()

# http协议的POST方法
import requests
r = requests.post('http://httpbin.org/post', data = {'key':'value'})
r.json()
