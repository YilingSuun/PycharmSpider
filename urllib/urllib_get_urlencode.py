# Use case: Search with multiple parameters

import urllib.request
import urllib.parse

base_url = "https://cn.bing.com/search?"

data = {
    'q': '周杰伦',
    'sex': '男',
    'location': '台湾'
}

# Convert the dictionary to unicode.
a = urllib.parse.urlencode(data)
url = base_url + a

# Request resource path
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)

# Get web page source code
content = response.read().decode('utf-8')
print(content)
