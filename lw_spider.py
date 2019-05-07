#! /usr/bin/python3
'''
已完成数据库修改增加
    :book_author,book_summary
'''

import pymysql

import requests

from bs4 import BeautifulSoup

import re


def get_chapter_page(novel_url):
    '''获取文学作品章节表HTML
            从小说页面获取到章节列表的HMTL
            返回html_text是网页的html
    '''
    try:
        # 获取网页HTML
        r = requests.get(novel_url,timeout=30)
        # 如果状态不是200，引发HTTPError异常
        r.raise_for_status()
        # 修改网页编码格式为预测编码
        r.encoding = r.apparent_encoding
        # 将网页文本内容赋值给变量html_text
        html_text = r.text
        # 返回网页文本内容
        #print(html_text)
        return html_text
    except:
        return "get_chapter_page产生异常"

def get_chapter_tag_list(html_text):
    '''由文学作品的章节HTML提取章节URL<a>标签列表
            参数是从get_chapter_page返回的html_text
            返回的是各种章节的标签列表tag_list
    '''
    try:
        soup = BeautifulSoup(html_text,'html.parser')
        # 去掉列表中的第一个，去重，与最后一章重复
        tag_list = soup.find_all('a',href=re.compile('(\d)*/(\d)*/(\d)*.html'))[1:]
        #print(tag_list)
        return tag_list
    except:
        return "get_chapter_tag_list产生异常"

def get_chapter_url_list(tag_list):
    '''由文学作品的章节URL<a>标签列表提取章节URL列表
            参数是从get_chapter_tag_list返回的tag_list
            返回的是章节真实url的列表url_list
    '''
    try:
        # 复制标签列表tag_list
        url_list = list.copy(tag_list)
        # 长度
        url_len = len(tag_list)
        for i in tag_list:
            # 提取url
            url_list[url_len-1] =site_url + i.get('href')
            # 下一个
            url_len = url_len-1
        # 将列表的顺序翻转
        url_list.reverse()
        #print(url_list)
        return url_list
    except:
        return "get_chapter_url_list产生异常"

def get_title_content(chapter_url):
    ''' 获取 章节 的信息，包括title和content
            参数是章节的真实地址
            返回的是章节的title和content
    '''
    r = get_chapter_page(chapter_url)
    soup = BeautifulSoup(r,'html.parser')
    title = get_title(soup)
    content = get_content(soup)
    print(content)
    print(title)
    return title,content
def get_title(soup):
# 获取title
    title = soup.h1.get_text()
    return title
def get_content(soup):
# 获取内容
    content = soup.find_all(id='content')
    content = content[0].get_text()
    return content

def get_novel_info(html_text):
    ''' 获取 小说 的基本信息，包括title、 author和summary
            参数是小说的html_text
            返回的是小说的title
    '''
    soup = BeautifulSoup(html_text,'html.parser')

    info = soup.find_all('p')
    #作者
    author = info[0].string
    #简介
    summary = info[5].string

    title = get_title(soup)
    print(title)
    return title,author,summary

def insert_books(novel_title,novel_author,novel_summary,novel_url):
    # 将book_name,book_url保存到mysql
    #sql语句插入book_name,book_url
    sql = "insert into books(book_name,book_url,book_author,book_summary) \
            values('%s','%s','%s','%s')"%(novel_title,novel_url,novel_author,novel_summary)
    try:
        # 使用execute()方法执行SQL
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except:
        db.rollback()

def get_book_id(novel_url):

    """
    以下为了提取出book_id
    """
    #novel_url = "http://www.xbiquge.la/0/0001/"
    sqlsql = "select book_id from books where book_url='%s'"\
            %(novel_url)
    try:
        # 使用execute()方法执行SQL
        cursor.execute(sqlsql)
        # 提交到数据库执行
        #db.commit()
    except:
        db.rollback()

    # 使用fetchone()方法获取单条数据
    book_id = cursor.fetchone()

    # 只取第一个值
    book_id= int(book_id[0])

    print(book_id)
    return book_id

    #db.close()
    """
    以上
    """

def insert_book(book_id,url_list):
    # book信息保存到mysql
    # 章节id初始化
    chapter_id = 0
    for i in url_list:
        chapter_title,chapter_content = get_title_content(i)
        chapter_id = chapter_id + 1

        sqlsqlsql = "insert into book(\
                book_id,chapter_id,chapter_name,chapter_content) \
                values(%s,%s,'%s','%s')"\
                %(book_id,chapter_id,chapter_title,chapter_content)
        try:
            # 使用execute()方法执行SQL
            cursor.execute(sqlsqlsql)
            # 提交到数据库执行
            db.commit()
        except:
            db.rollback()



if __name__=='__main__':
    #网站url
    site_url = "http://www.xbiquge.la"
    #novel_url
    novel_url = "http://www.xbiquge.la/0/0007/"

    #打开数据库连接
    db = pymysql.connect("127.0.0.1","zps",";lkj","lw_spiderdb")
    # 使用cursor()方法创建游标对象cursor
    cursor = db.cursor()

    # 获取文学作品章节表HTML
    html_text = get_chapter_page(novel_url)
    # 由文学作品的章节HTML提取章节URL<a>标签列表
    tag_list = get_chapter_tag_list(html_text)
    # 由文学作品的章节URL<a>标签列表提取章节URL列表
    url_list = get_chapter_url_list(tag_list)

    html_text = get_chapter_page(novel_url)
    #小说title
    #novel_title = get_novel_info(html_text)
    novel_title,novel_author,novel_summary = get_novel_info(html_text)
    # books信息保存到mysql
    insert_books(novel_title,novel_author,novel_summary,novel_url)

    # 获取book_id
    book_id = get_book_id(novel_url)
    # book信息保存到mysql
    insert_book(book_id,url_list)

    db.close()
