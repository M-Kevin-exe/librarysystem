from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="读者编号")
    username = models.CharField(max_length=255, verbose_name="姓名")
    phone = models.CharField(max_length=255, verbose_name="电话")

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'users'
        verbose_name = '用户信息'