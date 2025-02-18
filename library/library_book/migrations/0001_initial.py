# Generated by Django 5.1 on 2025-02-18 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='图书编号')),
                ('title', models.CharField(max_length=255, verbose_name='书名')),
                ('author', models.CharField(max_length=255, verbose_name='作者')),
                ('price', models.FloatField(verbose_name='价格')),
                ('count', models.IntegerField(verbose_name='数量')),
            ],
        ),
    ]
