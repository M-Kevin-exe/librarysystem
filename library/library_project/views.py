from django.shortcuts import render
from django.http import HttpResponse
from .models import BorrowBook, Users, Books
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime, timedelta


# Create your views here.

# 借书
@csrf_exempt
def borrow_book(request):
    if request.method == 'POST':
        reader = request.POST.get('reader')
        reader_interface = Users.objects.get(username=reader)
        book = request.POST.get('book')
        book_interface = Books.objects.get(title=book)
        borrow_date = request.POST.get('borrow_date')
        if not borrow_date:
            borrow_date = datetime.now().strftime('%Y-%m-%d')
        else:
            borrow_date = datetime.strptime(borrow_date, '%Y-%m-%d')
        # 借出30天归还
        return_date = borrow_date + timedelta(days=30)
        status = "未还"
        # 保存数据
        borrow_book = BorrowBook()
        borrow_book.reader = reader_interface
        borrow_book.book = book_interface
        borrow_book.borrow_date = borrow_date
        borrow_book.return_date = return_date
        borrow_book.status = status
        borrow_book.save()
        return HttpResponse('借书成功')


# 还书
@csrf_exempt
def return_book(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        borrow_book = BorrowBook.objects.get(id=id)
        borrow_book.status = '已还'
        borrow_book.save()
        return HttpResponse('还书成功')