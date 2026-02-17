from django.urls import path
from . import views

urlpatterns = [

    path('', views.book_list, name='book_list'),

    path('book/<int:id>/', views.book_detail, name='book_detail'),

    path('create/', views.create_book, name='create_book'),

    path('update/<int:id>/', views.update_book, name='update_book'),

    path('delete/<int:id>/', views.delete_book, name='delete_book'),
]
path('api/books/', views.api_books),
path('api/books/<int:id>/', views.api_book_detail),
path('rest/books/', views.rest_books),

