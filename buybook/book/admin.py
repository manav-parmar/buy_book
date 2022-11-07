from django.contrib import admin
from .models import Book,Buybook
@admin.register(Book)
class Books(admin.ModelAdmin):
        list_display=['id','bookname','bookprice','bookpage','authername','booklanguage','bookquantity','deleted']

@admin.register(Buybook)
class Buybooks(admin.ModelAdmin):
        list_display=['id','bookdetail','username','buydate','returndate','buy','phone','deleted']


# Register your models here.
