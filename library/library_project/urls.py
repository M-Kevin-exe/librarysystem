
from . import views
from django.urls import path

urlpatterns = [
    path('api/borrow/', views.borrow_book, name='borrow_book'),
    path('api/return/', views.return_book, name='return_book')
]
