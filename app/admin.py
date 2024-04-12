from django.contrib import admin
from .models import Expense, ActionLogs

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'category')

class ActionLogsAdmin(admin.ModelAdmin):
    list_display = ('method', 'status', 'endpoint')

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ActionLogs, ActionLogsAdmin)