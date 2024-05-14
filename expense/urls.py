from django.urls import path
from .views import (
    home, 
    ExpenseList, 
    ExpenseDetail, 
    CategoryList,
    CategoryDatail
)

urlpatterns = [
    path('', home, name='home'),

    path('api/expenses/', ExpenseList.as_view(), name='expense_list'),
    path('api/expense/<int:pk>/', ExpenseDetail.as_view(), name='expense_detail'),

    path('api/categores/', CategoryList.as_view(), name='category_list'),
    path('api/category/<int:pk>/', CategoryDatail.as_view(), name='category_detail')
]