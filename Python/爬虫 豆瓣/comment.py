import bs4
import requests
import file_operation
import Movie
import request_body
from tqdm import tqdm


def get_movie_short_comment(url):
    path = 'short_comment\\'
    id = Movie.get_movie_id(url)
    file = path + str(id) + '.txt'
    file_operation.make_empty_file(file)

    comment_str = ""
    page = 0
    num = 0
    for i in tqdm(range(1,10)):
        while (page != 200):
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
            #print("短评个数：" + str(num) + "页码" + str(page) + '\n')
            with open(file, 'a', encoding='utf8') as fj:
                fj.write(comment_str)
    print('--------------------------------------')

if __name__ == '__main__':
    list = file_operation.read_file('movie_url.txt')
    path = 'movie_url.txt'
    n = 0
    for url in list:
        get_movie_short_comment(url)
        n=n+1
        while(n==10):
            exit()