from tqdm import tqdm

import file_operation
import request_body
import requests
import bs4
import re

def get_url_html_soup(url):
    header=request_body.get_header()
    proxies=request_body.get_proxy()
    req=requests.get(url=url,proxies=proxies,headers=header)
    html=req.text
    if req.status_code==200:
        print("请求成功！")
        soup=bs4.BeautifulSoup(html,'lxml')
        return soup
    if req.status_code!=200:
        print("请求失败！")

def get_movie_id(url):
    movie_id = re.compile(r'\d')
    f = movie_id.findall(url)
    k = file_operation.segmented(f)
    id = k.replace(' ', '')
    return id

# 返回影片标题
def get_movie_title(soup):
    movie_name = soup.find('h1').text  # 获取电影标题
    return movie_name

# 返回影片的导演名
def get_movie_directors(soup):
    contents = soup.find('div', id='info')
    # 构造正则表达式
    directors = re.compile(r'导演:(.*)')
    # 在contents的文本内容中寻找与正则表达式匹配的内容（编译运行正则表达式）
    f = directors.findall(contents.text)[0]
    lists = str.split(f)
    director_name = file_operation.segmented(lists)
    return director_name

# 返回影片的编剧名
def get_movie_screenwriter(soup):
    contents = soup.find('div', id='info')
    screenwriter = re.compile(r'编剧:(.*)')
    f = screenwriter.findall(contents.text)[0]
    lists = str.split(f)
    screenwriter_name = file_operation.segmented(lists)
    return screenwriter_name

# 返回影片的主演名
def get_movie_character(soup):
    contents = soup.find('div', id='info')
    character = re.compile(r'主演:(.*)')
    f = character.findall(contents.text)[0]
    lists = str.split(f)
    characters_name = file_operation.segmented(lists)
    return characters_name

# 返回影片的类型
def get_movie_type(soup):
    contents = soup.find('div', id='info')
    type = re.compile(r'类型:(.*)')
    f = type.findall(contents.text)[0]
    lists = str.split(f)
    type_name = file_operation.segmented(lists)
    return type_name

# 返回影片的制片国家/地区
def get_movie_country(soup):
    contents = soup.find('div', id='info')
    pattern = re.compile('制片国家/地区:(.*)')
    f = pattern.findall(contents.text)[0]
    lists = str.split(f)
    country = file_operation.segmented(lists)
    return country

def get_movie_shortcomment(url):
    comment_str = ""
    page = 0
    num = 0
    for i in tqdm(range(1, 10)):
        while (page != 40):
            url2 = url + 'comments?start=' \
                   + str(page) + '&limit=20&sort=new_score&status=P'
            header = request_body.get_header()
            proxies = request_body.get_proxy()
            req = requests.get(url=url2, proxies=proxies, headers=header)
            html = req.text
            soup = bs4.BeautifulSoup(html, 'lxml')

            short_comment = soup.find_all('span', class_="short")
            for list in short_comment:
                comment_str = comment_str + list.text + '\n'
                num = num + 1

            page = page + 20
    return comment_str
if __name__ == '__main__':
    url='https://movie.douban.com/subject/4864908/'
    soup=get_url_html_soup(url)
    title=get_movie_title(soup)
    print(title)
