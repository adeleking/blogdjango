from django.urls import path, include
from .views import (
    create_blog_view,
    delete_blog_view,
    update_blog_view,
    detail_blog_view,
    list_blog_view,
)

urlpatterns =[
    path('<str:slug>/delete/', delete_blog_view, name='blog-delete'),
    path('update/<str:slug>', update_blog_view, name='blog-update'),
    path('detail/<str:slug>', detail_blog_view, name='blog-detail'),
    path('', list_blog_view, name='blog-list')
]