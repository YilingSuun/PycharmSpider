import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/ait/text/translate'

# request head
headers = {
        #'Accept': 'text/event-stream',
        #'Accept-Encoding': 'gzip, deflate, br, zstd',
        #'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        #'Acs-Token': '1716206471330_1716273859454_Bz9nK+x7jRMdopudIShfPtW6CfhSdAAvN5N1q1+CRvrzMNBfybkL2CM+VKIsomXfAop8ngy4jg49WXP5dzEwcwzQOUoEQ4koGlVjEJuOmaubSX+EwBU3ohn2vNNRZnCPV+00UMYTWRFgFYiUsoW8gmND2YmICGwx4TPoGW36SijL3dBIadSlOLMwO0OuDY7DHhiRSnYfK6Zs1iixFz8zU4xuFQ12RtR5lZUmraORBz6Q3hMwt/zG/89wGrH6GILwakfXVMIrvclBd5Q7d+yMYm+kKRUjnZZGK6HYd5/cho7wkA5pV6hz8gLLjvJ4IZfM4Zu+hsxNvueU6uEgIfc7UDPAED9fTJ/1CBzvmPL0r/YMCcCnoWaX+bB6FhXUgUUV65T7M9TUDQfVvMTizDJUzegFE+OJMvOOVUImxXB6yxAafdoWuS8ZPmarY8gp0Kb0ervE9+2+Yef91J1swCusnOP+5m+Dh7rtg6cSddJ5IeX6lEyy25wImPLV7EiR7uHH',
        #'Connection': 'keep-alive',
        #'Content-Length': '198',
        #'Content-Type': 'application/json',
        'Cookie': 'BAIDUID=D3F33C03A8BBE15400413FB6792F473D:FG=1; H_WISE_SIDS=131861_216838_213351_214796_110085_244714_254831_261719_236312_256419_265881_267372_265615_256302_267074_259033_268569_268592_268030_259642_256151_269730_269831_269328_269904_267066_256739_270460_270548_270923_270315_271035_271020_270442_271169_271178_269771_267659_271319_270102_271560_271727_271813_269876_267807_269664_271943_234295_234207_269297_272082_272223_272280_263618_272322_272365_272009_272337_272461_253022_272821_272802_260335_271284_267596_273058_267558_273090_273164_273118_273147_273235_272797_273300_273371_273400_273393_271158_270055_273489_273518_271146_273705_264170_270185_274080_273931_273966_274139_273842_274177_269610_274209_273917_274233_273786_273043_273593_272805_203517_274356_272319_272560_274441_274571; BIDUPSID=D3F33C03A8BBE15400413FB6792F473D; PSTM=1708833849; H_PS_PSSID=40463_60174_60269; BAIDUID_BFESS=D3F33C03A8BBE15400413FB6792F473D:FG=1; ZFY=k0BuHvzb94fjFYe854pgfHOh5PsQ1fF1SQELCv6wvRQ:C; MCITY=-349%3A; BAIDU_WISE_UID=wapp_1716171863882_727; ab_sr=1.0.1_M2RiZTRkNTUyMGY3NmFiMTM3NzEyZWUyN2JiZmNiNTM2ODczNjgyOTBiOGQ3NDdiMGYwNzI2NWQ2N2U4ZjlkMjA2YjZjMzA2ZGY5NTkyMTljNmYyNjU1NmQ1YWQ3NjQ3MTA1ZDYwOGNlMWM1ODg2OWRlZTNhZTcxMWVlNzVmM2I4OWI2NGJkNjBhMjQwMGRiMzY3ZjA4MzkyMjIwYmM4YQ==; RT="z=1&dm=baidu.com&si=69d1d8c7-f5dc-45ca-b0fc-0f6d79b79b5d&ss=lwg0z0mb&sl=5&tt=3se&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=618q"',
        #'Host': 'fanyi.baidu.com',
        #'Origin': 'https://fanyi.baidu.com',
        #'Referer': 'https://fanyi.baidu.com/mtpe-individual/multimodal?query=love&lang=en2zh',
        #'Sec-Ch-Ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        #'Sec-Ch-Ua-Mobile': '?0',
        #'Sec-Ch-Ua-Platform': '"Windows"',
        #'Sec-Fetch-Dest': 'empty',
        #'Sec-Fetch-Mode': 'cors',
        #'Sec-Fetch-Site': 'same-origin',
        #'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
}

data = {'corpusIds': '[]', 'domain': "common", 'from': "en",
        'milliTimestamp': '1716262807144', 'needPhonetic': 'true',
        'qcSettings': '''["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]''',
        'query': "love", 'reference': "", 'to': "zh"
        }

# The Post request parameters must be encoded and converted to bytes using the encode method
data = urllib.parse.urlencode(data).encode('utf-8')

# Request object
request = urllib.request.Request(url=url, data=data, headers=headers)

# Simulate the browser sending a request to the server
response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
print(content)


