import urllib.request

url_web = 'http://www.douyin.com/discover'
url_image1 = ('https://ts1.cn.mm.bing.net/th?id=OIP-C.ymfMz02YOcnJZlPQNb'
             'lE3gHaHa&w=198&h=185&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2')
url_image2 = ("https://ts3.cn.mm.bing.net/th?id=OIP-C.1XYfBs4X_3CspGu7JX13"
              "IwHaNK&w=187&h=333&c=8&rs=1&qlt=90&o=6&dpr=1.5&pid=3.1&rm=2")
url_page = ('https://www.sohu.com/a/779401855_114731?edtsign=CDF40CCA41E0DAF'
            '24C4C623CC059104C8CF87FF1&edtcode=t2ghGd6SBUJwCxJjFvW8hQ%3D%3D&scm=tho'
            'r.282_14-200000.0.10006.&ace=55F392AAC1852314039A0FAC50A35'
            '24D9DCBF7A&code=66h39ajik1o&spm=smpc.home.top-news1.6.1715928890888lom'
            'IQwm_1467')


urllib.request.urlretrieve(url_web, '../tiktok.html')
urllib.request.urlretrieve(url_image2, 'image2.jpg')
urllib.request.urlretrieve(url=url_image1, filename='image.jpg')
urllib.request.urlretrieve(url_page, '../page.html')
