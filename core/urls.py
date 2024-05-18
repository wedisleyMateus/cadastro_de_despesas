from django.contrib import admin
from django.urls import path, re_path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib.auth import views as auth_views

schema_view = get_schema_view(
   openapi.Info(
      title="Cadastro de Despesas",
      default_version='v1',
      description="Fornece Gestão sobre a despesas",
      terms_of_service="https://www.suaempresa.com/terms/",
      contact=openapi.Contact(email="contato@suaempresa.local"),
      license=openapi.License(name="Licença BSD"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include('expense.urls')),
    path('', include('revenue.urls')),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]