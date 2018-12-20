import pymysql

import Movie

host = 'localhost'
user = 'root'
password = ''
database = 'douban2'


def create_table():
    db=pymysql.connect(host,user,password,database)
    cursor=db.cursor()
    cursor.execute("drop table if exists contents")
    sql="""
         create table contents(
            movie_id char(60) not null,
            movie_title char(200),
            movie_director char(200),
            movie_screenwriter char(200),
            movie_character varchar(1000),
            movie_type char(200),
            movie_country char(200)
                ) 
            """
    cursor.execute(sql)
    db.commit()
    db.close()


def create_table_comment():
    db=pymysql.connect(host,user,password,database)
    cursor=db.cursor()
    cursor.execute("drop table if exists comment")
    sql="""
         create table comment(
            movie_id char(60) not null,
            movie_comment text
                ) 
            """
    cursor.execute(sql)
    db.commit()
    db.close()


def insert_database(id,title,director,screenwriter,mcharacter,mtype,country):
    db=pymysql.connect(host,user,password,database)
    cursor=db.cursor()
    sql=' insert into contents values("%s","%s","%s","%s","%s","%s","%s")'\
        %(id,title,director,screenwriter,mcharacter,mtype,country)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

#text类型最大长度65535，放不下太多评论
def insert_comment(id,comment):
    db=pymysql.connect(host,user,password,database)
    cursor=db.cursor()
    sql=' insert into comment values("%s","%s")'\
        %(id,comment)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()


def select_database(id):
    db = pymysql.connect(host, user, password, database)
    cursor = db.cursor()

    sql='select movie_id from contents ' \
        'where movie_id="%s"'%id

    try:
        cursor.execute(sql)
        results=cursor.fetchall()
        for row in results:
            m_id=row[0]
            print(("movie_id=%s")%m_id + 'ok!' + '\n')
    except:
        print("Error:unable to fetch"+ id)
    db.close()

if __name__ == '__main__':
    # create_table()
    create_table_comment()
    url='https://movie.douban.com/subject/4864908/'
    comment = Movie.get_movie_shortcomment(url)
    id=Movie.get_movie_id(url)
    # id='a'
    # comment='b'
    insert_comment(id,comment)
