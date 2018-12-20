#import movie_url
#movie_url.get_movie_url(number=120)

import file_operation
import Movie
import connect_mysql

list=file_operation.read_file('movie_url.txt')
path = 'movie_url.txt'
n = 0
for url in list:
    soup=Movie.get_url_html_soup(url)
    id=Movie.get_movie_id(url)
    title=Movie.get_movie_title(soup)
    director=Movie.get_movie_directors(soup)
    screenwriter=Movie.get_movie_screenwriter(soup)
    character=Movie.get_movie_character(soup)
    type=Movie.get_movie_type(soup)
    country=Movie.get_movie_country(soup)
    comment=Movie.get_movie_shortcomment(url)

    connect_mysql.insert_database(id,title,director,screenwriter,character,type,country)
    connect_mysql.insert_comment(id,comment)
    n=n+1
    while(n==10):
        exit()