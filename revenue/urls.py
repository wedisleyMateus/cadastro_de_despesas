from django.urls import path
from .views import UserList, UserDetail
from .views import RecurrenceList, RecurrenceDetail
from .views import ContractList, ContractDetail
from .views import RecipeCategoryList, RecipeCategoryDetail
from .views import RecipeList, RecipeDetail
from .views import PaymentList, PaymentDetail
from .views import ContractRecipeList, ContractRecipeDetail

urlpatterns = [
    path('api/users/', UserList.as_view(), name='UserList'),
    path('api/user/<int:pk>/', UserDetail.as_view(), name='UserDetail'),

    path('api/recurrences/', RecurrenceList.as_view(), name='RecurrenceList'),
    path('api/recurrence/', RecurrenceDetail.as_view(), name='RecurrenceDetail'),

    path('api/contracts/', ContractList.as_view(), name='ContractList'),
    path('api/contract/', ContractDetail.as_view(), name='ContractDetail'),

    path('api/recipe-category/', RecipeCategoryList.as_view(), name='RecipeCategoryList'),
    path('api/revenue-category/', RecipeCategoryDetail.as_view(), name='RecipeCategoryDetail'),

    path('api/recipe/', RecipeList.as_view(), name='RecipeList'),
    path('api/revenues/', RecipeDetail.as_view(), name='RecipeDetail'),

    path('api/payments/', PaymentList.as_view(), name='PaymentList'),
    path('api/payment/', PaymentDetail.as_view(), name='PaymentDetail'),

    path('api/contract-recipes/', ContractRecipeList.as_view(), name='ContractRecipeList'),
    path('api/contract-recipe/', ContractRecipeDetail.as_view(), name='ContractRecipeDetail')
]
