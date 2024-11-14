# post request

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

#head
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

data = {
    'kw': 'spider'
}

# post parameters must be encoded
data = urllib.parse.urlencode(data)

# post parameters must be encoded (str to byte)
data = data.encode('utf-8')

# The post request parameters are not appended to the url,
# but to a custom request object parameter (data in bytes).
request = urllib.request.Request(url=url, data=data, headers=headers)

# Simulate the browser sending a request to the server
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)

# String --> json object

import json

obj = json.loads(content)
print(obj)
