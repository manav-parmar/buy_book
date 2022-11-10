"""buybook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from book import views
from book import user_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('base/',views.Baseview.as_view(),name='base'),
    path('login/',views.Loginview.as_view(),name='login'),
    path('userregister/', views.Userregisterview.as_view(), name='userregister'),
    path('admin-register/', views.Adminregisterview.as_view(), name='adminregister'),

    path('forgotpassword/', views.Forgotpasswordview.as_view(), name='forgotpassword'),
    path('add-book/', views.Addbookview.as_view(), name='addbook'),

    path('register-user-table/', views.Registerusertableview.as_view(), name='registerusertable'),
    path('register-admin-table/', views.Registeradmintableview.as_view(), name='registeradmintable'),
    path('show-book-table/', views.Showbooktableview.as_view(), name='showbooktable'),

    path('buy-book-user-table/', views.Buybookusertableview.as_view(), name='buybookusertable'),
    path('edit-book/<int:id>/', views.Editbookview.as_view(), name='editbook'),
    path('delete-book/<int:id>/', views.Deletebookview.as_view(), name='deletebook'),
    path('delete-user/<int:id>/', views.Deleteuserview.as_view(), name='deleteuser'),
    path('delete-admin/<int:id>/', views.Deleteadminview.as_view(), name='deleteadmin'),
 
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('add-return-book-list/', user_view.AddreturnbookViewlist.as_view(), name='add-return-book-list'),
    path('add-return-book/<int:id>/', views.AddreturnbookView.as_view(), name='add-return-book'),
    path('add-return-book-sucess/<int:id>/', views.AddreturnbooksucessView.as_view(), name='add-return-book-sucess'),
    path('admin-profile/<int:id>/', views.Adminprofile.as_view(), name='admin-profile'),
    # <--------------------------user path -------------------------->
    path('user/', user_view.userbase.as_view(), name='user'),
    path('user-profile/<int:id>/', user_view.userprofile.as_view(), name='user-profile'),
    path('buy-book/', user_view.Buybooks.as_view(), name='buybook'),
    path('buy-book-detail/<int:id>/', user_view.Buybookdetail.as_view(), name='buybookdetail'),

    path('show-buy-book-table/', user_view.Showbuybooktable.as_view(), name='showbuybooktable'),
    path('user-logout/', user_view.LogoutView.as_view(), name='user-logout'),
    path('return-book/<int:id>/', user_view.ReturnbookView.as_view(), name='return-book'),
    # <--------------------------Api path -------------------------->
    path('api/', include('buy_book_api.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


