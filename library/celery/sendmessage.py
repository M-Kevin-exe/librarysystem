from celery import shared_task
from datetime import datetime, timedelta
from ..library_book.models import Books
from ..library_project.models import BorrowBook
from ..users.models import Users

# 图书借阅期限为 30 天，每天 08:00 发通知将在 7 天内到期的图书借阅者，提醒还书 
@shared_task
def send_message():
    today = datetime.now().date()
    seven_days_later = today + timedelta(days=7)
    # 获取大于还书日期并未归还的数据
    borrow_books = BorrowBook.objects.filter(return_date__lte=seven_days_later, status='借阅中')
    for borrow_book in borrow_books:
        book = Books.objects.get(id=borrow_book.book_id)
        reader = Users.objects.get(id=borrow_book.reader_id)

        book_title = book.title
        reader_name = reader.username
        reader_phone = reader.phone

        # 发送短信通知读者
        print(f'图书《{book_title}》将在 {borrow_book.return_date} 前到期，请读者 {reader_name} ({reader_phone}) 尽快还书。')