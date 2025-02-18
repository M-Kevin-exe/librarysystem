from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.

# 增加图书
@csrf_exempt
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        count = request.POST.get('count')
        book = Books(title=title, author=author, price=price, count=count)
        book.save()
        return HttpResponse('添加成功')

# 修改图书
@csrf_exempt
def update_book(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        count = request.POST.get('count')
        book = Books.objects.get(id=id)
        book.title = title
        book.author = author
        book.price= price
        book.count = count
        book.save()
        return HttpResponse('修改成功')

# 查看图书
def get_book(request):
    if request.method == 'GET':
        books = Books.objects.all()
        books_list = []
        for book in books:
            books_list.append(book.to_json())
        
        response_json = json.dumps({'books': books_list,'status':'success'})
        return HttpResponse(response_json, content_type='application/json')

# 删除图书
@csrf_exempt
def delete_book(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        book = Books.objects.get(id=id)
        book.delete()
        return HttpResponse('删除成功')