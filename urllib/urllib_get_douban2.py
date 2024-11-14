# This is a get request to get the first ten pages of the Douban movie and save it.

#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=0&limit=20

#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=20&limit=20

#https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&
# start=40&limit=20

# 规律：start = (page - 1) * 20


import urllib.request
import urllib.parse


# 请求对象的定制
def create_request(my_page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start='
    start = str((my_page - 1) * 20)
    url = base_url + start + '&limit=20'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    my_request = urllib.request.Request(url=url, headers=headers)
    return my_request


# 获取响应数据
def get_content(my_request):
    response = urllib.request.urlopen(my_request)
    content = response.read().decode('utf-8')
    return content


# 下载
def download(page, content):
    with open('douban' + str(page) + '.json', 'w', encoding='utf-8')as fp:
        fp.write(content)


# 程序的入口
if __name__ == '__main__':
    start_page = int(input('请输入起始的页码'))
    end_page = int(input('请输入结束的页码'))

    for page in range(start_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(page, content)
