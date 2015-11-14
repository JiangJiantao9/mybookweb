# -*- coding: utf-8 -*-
#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from models import Author,Book
# Create your views here.
def Home(request):
    books = Book.objects.all()
    return render(request, 'home.html',{'books':books})

def Serch_table(request):
    return render(request, 'serch.html')
    
def add_b(request):
    return render(request, 'add_book.html',{'i':0})
def add_a(request):
    return render(request, 'add_author.html',{'i':0})

def Serch(request):
    name_s = request.GET['name_s']
    t_Author = Author.objects.filter(Name = name_s)
    if t_Author:
        s_Author = t_Author[0]
        Author_name = s_Author.Name
        s_book = Book.objects.filter(AuthorID = s_Author)
        books = []
        for i in s_book:
            books.append(i.Title)
        return render(request, 'books.html', {'Author_name':Author_name,'books':books})
    else:
        return render(request, 'serch_fail.html')

def Add_book(request):
    nISBN = request.GET['ISBN']
    ntitle = request.GET['title']
    nauthor = request.GET['author']
    npublisher = request.GET['publisher']
    npublishdate = request.GET['publishdate']
    nprice = request.GET['price']
    if nISBN and ntitle and nauthor and npublisher and npublishdate and nprice:
        t_new_author = Author.objects.filter(Name = nauthor)
        if t_new_author:
            new_author = t_new_author[0]
            Book.objects.create(ISBN=nISBN,
                                Title=ntitle,
                                AuthorID=new_author,
                                Publisher=npublisher,
                                PublishDate=npublishdate,
                                Price=nprice)
            return render(request,'scceed.html')
        
        return render(request, 'fail.html')
    else:
        return render(request, 'add_book.html',{'i':1})

        
    
def Add_author(request):
    nname = request.GET['name']
    nage = request.GET['age']
    ncountry = request.GET['country']
    if nname and nage and ncountry:
        Author.objects.create(Name=nname,Age=nage,Country=ncountry)
        return render(request,'scceed.html')
    else:
        return render(request, 'add_author.html', {'i':1})
    
def Information_serch(request):
    book_name = request.GET['bookname']
    book = Book.objects.get(Title = book_name)
    author = book.AuthorID
    return render(request,'information.html',{'book':book,'author':author})

def Delete_book(request):
    bookID = request.GET['bookID']
    book = Book.objects.get(ISBN = bookID)
    book.delete()
    return render(request,'scceed.html')
     
def Update_b(request):
    bookID = request.GET['bookID']
    book = Book.objects.get(ISBN = bookID)
    return render(request,'update.html',{'book':book})
    
def Update_book(request):
    nISBN = request.GET['ISBN']
    ntitle = request.GET['title']
    nauthor = request.GET['author']
    npublisher = request.GET['publisher']
    npublishdate = request.GET['publishdate']
    nprice = request.GET['price']
    if nISBN and ntitle and nauthor and npublisher and npublishdate and nprice:
        t_new_author = Author.objects.filter(Name = nauthor)
        if t_new_author:
            new_author = t_new_author[0]
            book=Book.objects.get(ISBN = nISBN)
            book.Author = new_author
            book.Publisher = npublisher
            book.PublishDate = npublishdate
            book.Price = nprice 
            book.save()
            return render(request,'scceed.html')
        
        return render(request, 'fail.html')
    else:
        return render(request, 'update.html',{'i':1})
    
   
    
    