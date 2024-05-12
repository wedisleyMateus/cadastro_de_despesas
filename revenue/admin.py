from django.contrib import admin
from .models import BankingAssociation, RevenueValue, NetRevenue

class BankingAssociationAdmin(admin.ModelAdmin):
    list_display = ('service', 'value', 'date')

admin.site.register(BankingAssociation, BankingAssociationAdmin)
