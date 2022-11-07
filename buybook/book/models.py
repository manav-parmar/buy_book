from email.policy import default
from django.db import models

class Book(models.Model):
    bookname=models.CharField(max_length=200)
    bookprice=models.IntegerField()
    bookpage = models.IntegerField()
    authername=models.CharField(max_length=300)
    booklanguage = models.CharField(max_length=300)
    bookquantity=models.CharField(max_length=10)
    deleted= models.BooleanField(default=False)


    def __str__(self):
        return self.bookname

class Buybook(models.Model):
    bookdetail=models.ForeignKey(Book,null=True, on_delete=models.SET_NULL)
    username=models.CharField(max_length=150)
    buydate=models.DateField()
    returndate=models.DateField()
    buybookquantity = models.CharField(max_length=10)
    buy=models.BooleanField()
    phone=models.CharField(max_length=10)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.username




