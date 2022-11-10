from django.contrib import admin
from django.urls import path,include
from buy_book_api import views
from rest_framework.routers import DefaultRouter
from buy_book_api import views as vw
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register('user-register', vw.UserViewSet, basename='user-register')
router.register('admin-register', vw.AdminViewSet, basename='admin-register')
router.register('book', vw.Bookapi, basename='book')
router.register('buy-book-user', vw.BuyBookUserapi, basename='buy-book-user')
router.register('show-book', vw.Showbooks, basename='show-book')
router.register('show-buy-book', vw.BuybookViewset, basename='show-buy-book')
router.register('user-profile', vw.Userprofileapi, basename='user-profile')
router.register('buy-book', vw.Buybookapi, basename='buy-book')
urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin-profile/<int:pk>/', vw.Adminprofileapi.as_view(), name='admin-profile'),
    path('admin-profile/<int:pk>/', vw.Adminprofileapi.as_view(), name='admin-profile'),
    path('return-book/<int:id>/', vw.Returnbookapi.as_view(), name='return-book'),
]