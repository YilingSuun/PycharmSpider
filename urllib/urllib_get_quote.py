# Get https://cn.bing.com/search?q=周杰伦 Web page source code
import urllib.request
import urllib.parse

url = "https://cn.bing.com/search?q="

# Transfer 周杰伦 into unicode
# Method: urllib.parse
name = urllib.parse.quote('周杰伦')

url = url + name

# Request object customization, the first means to solve anti-crawling
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}
request = urllib.request.Request(url=url, headers=headers)

# Simulate the browser sending a request to the server
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
