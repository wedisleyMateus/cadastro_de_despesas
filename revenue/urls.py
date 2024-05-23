from django.urls import path
from .views import UserList, UserDetail
from .views import CategoryList, CategoryDetail

urlpatterns = [
    path('api/users/', UserList.as_view(), name='UserList'),
    path('api/user/<int:pk>/', UserDetail.as_view(), name='UserDetail'),
    path('api/categories/', CategoryList.as_view(), name='CategoryList'),
    path('api/category/', CategoryDetail.as_view(), name='CategoryDetail')
]
