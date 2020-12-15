
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('listview/', views.MyListView.as_view(), name='mylistview'),
    path('listview/<int:pk>/', views.ListElementView.as_view(), name='list_element'),
    path('listview/createobject/', views.ObjectCreate.as_view(), name='create_element'),
]
