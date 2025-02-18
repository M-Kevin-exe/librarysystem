
from . import views
from django.urls import path

urlpatterns = [
    path('api/addbook/', views.add_book, name='add_book'),
    path('api/deletebook/', views.delete_book, name='delete_book'),
    path('api/getbook/', views.get_book, name='get_book'),
    path('api/updatebook/', views.update_book, name='update_book'),
]
