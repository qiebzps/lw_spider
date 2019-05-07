from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Books
from django.template.loader import get_template
from datetime import datetime
from django.shortcuts import redirect

# Create your views here.
#def homepage(request):
#    books = Books.objects.all()
#    books_list = list()
#
#    for count,book in enumerate(books):
#        books_list.append("No.{}:".format(str(count)) + str(book.book_name) + "<hr>")
#        books_list.append("<small>" + str(book.book_author) + "</small><br><br>")
#        books_list.append("<small>"+"简介：<br>" + str(book.book_summary) + "</small><br><br>")
#
#        chapters =Book.objects.filter(book_id=book.book_id) 
#        for count,i in enumerate(chapters):
#            books_list.append("{}:".format(str(count)) + str(i.chapter_name)+"<br>")
#
#    return HttpResponse(books_list)

def homepage(request):
    template = get_template('index.html')
    books = Books.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)
def showbook(request,book_id):
    template = get_template('book.html')
    try:
        book = Books.objects.get(book_id=book_id)
        chapters = Book.objects.filter(book_id=book_id)
        if book != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
def showchapter(request,book_id,chapter_id):
    template = get_template('chapter.html')
    try:
        book = Books.objects.get(book_id=book_id)
        chapters = Book.objects.filter(book_id=book_id)
        #content = chapters.objects.get(chapter_id=chapter_id)
        chapter_id = int(chapter_id)
        content = chapters[chapter_id].chapter_content
        title = chapters[chapter_id].chapter_name
        if content != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        # 如果找不到chapter_id则返回至book页面
        return redirect('/book/{}'.format(str(book_id)))
        return redirect('/')
