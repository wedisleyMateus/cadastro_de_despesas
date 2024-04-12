from django.urls import path
from .views import (
    home, 
    expense_list, 
    expense_detail, 
    category_list,
    category_detail
)

urlpatterns = [
    path('', home, name='home'),

    path('api/expenses/', expense_list, name='expense_list'),
    path('api/expense/<int:pk>/', expense_detail, name='expense_detail'),

    path('api/categores/', category_list, name='category_list'),
    path('api/category/<int:pk>/', category_detail, name='category_detail')
]