from django.shortcuts import render

from rest_framework import serializers
from book.models import Buybook, Book
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse


class Userregisterserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password']


    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data["password"] = make_password(password)
        instance = super().create(validated_data)
        instance.save()
        return instance

class Adminregisterserializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'password', 'is_superuser']

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data["password"] = make_password(password)
        instance = super().create(validated_data)
        instance.save()
        return instance


class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'bookname', 'bookquantity', 'booklanguage', 'bookprice', 'bookpage', 'authername', 'deleted']


class Buybookserializer(serializers.ModelSerializer):


    class Meta:
        model = Buybook
        fields = ['id', 'bookdetail', 'username', 'buydate', 'returndate', 'buybookquantity', 'phone','buy','deleted']

    def validate(self, data):
        book=data['bookdetail']
        buybookquantity=data['buybookquantity']
        if book.bookquantity < buybookquantity:
            raise serializers.ValidationError(f'book must be {book.bookquantity}')
        return data
    def create(self, validated_data):
        book=validated_data['bookdetail']
        buybookquantity=validated_data['buybookquantity']
        total=int(book.bookquantity)-int(buybookquantity)
        if total == 0:
            book.deleted=True
        else:
            book.deleted = False
        book.bookquantity=total
        book.save()
        instance = super().create(validated_data)

        return instance

class showBookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ 'bookname', 'booklanguage', 'bookprice', 'bookpage', 'authername']

class Showbuybookserializer(serializers.ModelSerializer):
    bookdetail = showBookserializer(read_only=True)

    class Meta:
        model = Buybook
        fields = ['id', 'bookdetail', 'username', 'buydate', 'returndate', 'buybookquantity', 'phone']



class Buybookuserserializer(serializers.ModelSerializer):
    bookdetail = serializers.StringRelatedField(read_only=True)

    booklanguage = serializers.SerializerMethodField("get_booklanguage")
    bookprice = serializers.SerializerMethodField("get_bookprice")
    authername = serializers.SerializerMethodField("get_authername")

    def get_authername(self, obj):
        return obj.bookdetail.authername

    def get_booklanguage(self, obj):
        return obj.bookdetail.booklanguage

    def get_bookprice(self, obj):
        return obj.bookdetail.bookprice

    class Meta:
        model = Buybook
        fields = ['id', 'bookdetail', 'booklanguage', 'bookprice', 'authername', 'username', 'phone']


class Adminprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'first_name',
                  'last_name', 'email', 'is_superuser']

class Userprofileserializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = ['id', 'username', 'first_name',
                  'last_name', 'email']





