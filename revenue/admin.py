from django.contrib import admin
from .models import BankingAssociation, RevenueValue, NetRevenue

class BankingAssociationAdmin(admin.ModelAdmin):
    list_display = ('service', 'value', 'date')

class RevenueValueAdmin(admin.ModelAdmin):
    list_display = ('fixed_revenue', 'variable_revenue', 'date')

class NetRevenueAdmin(admin.ModelAdmin):
    list_display = ('amount', 'datetime')

admin.site.register(BankingAssociation, BankingAssociationAdmin)
admin.site.register(RevenueValue, RevenueValueAdmin)
admin.site.register(NetRevenue, NetRevenueAdmin)
