import urllib.request

url = 'https://www.baidu.com'
# https Reverse crawling
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                 ' (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
}
# Because the urlopen method can't store a dictionary, headers can't be passed in
# Request object
request = urllib.request.Request(url=url, headers=headers)

# The urlopen method accepts either an url or a request object
response = urllib.request.urlopen(request)

content = response.read().decode('utf8')

print(content)
response.close()
