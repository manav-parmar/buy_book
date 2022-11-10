import json

from django.shortcuts import render
from buy_book_api.serializer import *
from rest_framework.permissions import AllowAny
from book.models import Buybook,Book
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userregisterserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
class Showbooks(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Bookserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

class Buybookapi(viewsets.ModelViewSet):
    queryset = Buybook.objects.all()
    serializer_class = Buybookserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class Userprofileapi(viewsets.ModelViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class=Userprofileserializer

    def get_queryset(self):
        return User.objects.filter(username=self.request.user.username)





class AdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Adminregisterserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

class Bookapi(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class=Bookserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]



class BuyBookUserapi(viewsets.ReadOnlyModelViewSet):
    queryset = Buybook.objects.all()
    serializer_class=Buybookuserserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]

class Adminprofileapi(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class=Adminprofileserializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]





class BuybookViewset(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = Showbuybookserializer

    def get_queryset(self):
        return Buybook.objects.filter(username=self.request.user.username)


class Returnbookapi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self,request,id):
        buybook=Buybook.objects.get(id=id)
        book=Book.objects.get(id=buybook.bookdetail.id)
        book.bookquantity=int(book.bookquantity)+int(buybook.buybookquantity)
        book.deleted=False
        book.save()
        buybook.delete()
        return JsonResponse({'Return-book-info':'Your book will be Return successfully'})







