from django.urls import path
from .views import (
    home, 
    ExpenseList, 
    ExpenseDetail, 
    CategoryList,
    CategoryDatail,
    ExpenseUserList,
    ExpenseUserDetail,
    AdministrativeCostsList,
    AdministrativeCostsDetail
)

urlpatterns = [
    path('', home, name='home'),

    path('api/expense-users/', ExpenseUserList.as_view(), name='expense_users_list'),
    path('api/expense-user/<int:pk>/', ExpenseUserDetail.as_view(), name='expense_user_detail'),

    path('api/expenses/', ExpenseList.as_view(), name='expense_list'),
    path('api/expense/<int:pk>/', ExpenseDetail.as_view(), name='expense_detail'),

    path('api/categores/', CategoryList.as_view(), name='category_list'),
    path('api/category/<int:pk>/', CategoryDatail.as_view(), name='category_detail'),

    path('api/administrative/', AdministrativeCostsList.as_view(), name='Administrative_Costs_List'),
    path('api/administrative/<int:pk>/', AdministrativeCostsDetail.as_view(), name='Administrative_Costs_Detail')
]
