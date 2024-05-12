from django.urls import path
from .views import associations_list, association_detail

urlpatterns = [
    path('api/associations/', associations_list, name='Association_list'),
    path('api/association/<int:pk>/', association_detail, name='association_detail')
]