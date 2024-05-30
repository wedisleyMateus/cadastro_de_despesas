from django.contrib import admin
from .models import ExpenseUser, Expense, ActionLogs, Category

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'category')

class ActionLogsAdmin(admin.ModelAdmin):
    list_display = ('method', 'status', 'endpoint')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ActionLogs, ActionLogsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ExpenseUser)
