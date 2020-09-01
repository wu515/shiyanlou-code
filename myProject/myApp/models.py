from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200) #书名，char类型
    author = models.CharField(max_length=100) #作者
    pub_house = models.CharField(max_length=200) #出版社
    pub_date = models.DateTimeField('date published') #出版日期，时间日期类型