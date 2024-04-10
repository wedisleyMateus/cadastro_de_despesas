from django.urls import path
from .views import home, expense_list, expense_detail

urlpatterns = [
    path('', home, name='home'),

    path('api/expenses/', expense_list, name='expense_list'),
    path('api/expense/<int:pk>/', expense_detail, name='expense_detail'),
]