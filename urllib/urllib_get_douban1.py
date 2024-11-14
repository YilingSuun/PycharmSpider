# This is a GET REQUEST to get the data of the first page of the Douban movie and save it

import urllib.request
import urllib.parse

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
}

request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# download data
# By default, the open method uses gbk encoding. If you want to save Chinese characters,
# you need to specify utf-8 encoding in the open method.
fp = open('douban.json', 'w', encoding='utf-8')
fp.write(content)
