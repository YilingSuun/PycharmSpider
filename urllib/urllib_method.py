import urllib.request

url = 'http://www.baidu.com'
# Simulate the browser sending a request to the server
response = urllib.request.urlopen(url)

print(type(response))
# Get the page's source code
content = response.read ().decode('utf-8')
print(content)

print(response.geturl())
response.close()
