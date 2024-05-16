from django.urls import path
from .views import (
    AssociationsList,
    AssociationsDetail,
    RevenueList,
    RevenueDetail
)

urlpatterns = [
    path('api/associations/', AssociationsList.as_view(), name='Association_list'),
    path('api/association/<int:pk>/', AssociationsDetail.as_view(), name='association_detail'),
    path('api/revenues/', RevenueList.as_view(), name='Revenue_List'),
    path('api/revenue/', RevenueDetail.as_view(), name='Revenue_Detail')
]