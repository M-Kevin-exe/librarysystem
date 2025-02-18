from django.db import models
from library_book.models import Books
from users.models import Users

# Create your models here.
class BorrowBook(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="借书编号")
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name="图书编号")
    borrow_date = models.DateField(verbose_name="借书日期")
    return_date = models.DateField(verbose_name="还书日期")
    reader = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="读者编号")
    status = models.CharField(max_length=20, verbose_name="借书状态")

    def __str__(self):
        return f"{self.book.title} - {self.reader.username}"

    class Meta:
        db_table = 'borrow_book'
        verbose_name = '借书记录'