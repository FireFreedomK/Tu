import requests

url = 'https://movie.douban.com/subject/4864908/'
req=requests.get(url)
req.text
print(req.text)