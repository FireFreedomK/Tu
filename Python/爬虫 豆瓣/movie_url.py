from urllib import request
import urllib
import json
import request_body
import file_operation
from tqdm import tqdm

#number为页面的页数，默认为第一页。页面加一，number+20···
def get_movie_url(number=20):
    page = 0
    filename='movie_url.txt'
    file_operation.make_empty_file(filename)
    while(page!=number):
        proxies_support = urllib.request.ProxyHandler(request_body.get_proxy())
        opener = urllib.request.build_opener(proxies_support)
        urllib.request.install_opener(opener)  # 将代理Ip设置到全局

        url = 'https://movie.douban.com/j/search_subjects?type=movie&' \
              'tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(page)
        headers = request_body.get_header()
        res = request.Request(url,headers=headers)
        req = request.urlopen(res,timeout=0.5).read().decode("utf8")
        js = json.loads(req)
        url = ''
        for subjects in js['subjects']:
            url = url + subjects['url'] +'\n'
        #print(url)
        with open(filename, 'a', encoding='utf-8') as file_obj:
            file_obj.writelines(url)
            file_obj.write('\n')
        page=page+20


if __name__ == '__main__':
    for i in tqdm(range(1,8)):
        get_movie_url(number=120)