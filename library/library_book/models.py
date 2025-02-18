from django.db import models

# Create your models here.

class Books(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="图书编号")
    title = models.CharField(max_length=255, verbose_name="书名")
    author = models.CharField(max_length=255, verbose_name="作者")
    price = models.FloatField(verbose_name="价格")
    count = models.IntegerField(verbose_name="数量")

    def __str__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'count': self.count,
        }

    class Meta:
        db_table = 'books'
        verbose_name = '图书信息'