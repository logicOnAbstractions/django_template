
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    # the actual Index view that redirects to login is commented, we have a non-login one just for setup & debug
    # path('', views.IndexView.as_view(), name='index'),
    path('', views.DummyIndexView.as_view(), name='index'),
    path('listview/', views.MyListView.as_view(), name='mylistview'),
    path('listview/<int:pk>/', views.ListElementView.as_view(), name='list_element'),
    path('listview/createobject/', views.ObjectCreate.as_view(), name='create_element'),
    path('login/', views.LoginView.as_view(), name="login")
]
