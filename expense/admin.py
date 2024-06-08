from django.contrib import admin
from .models import ExpenseUser, Expense, ActionLogs, Category, AdministrativeCosts


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('description', 'date', 'category')


class ActionLogsAdmin(admin.ModelAdmin):
    list_display = ('method', 'status', 'endpoint')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class AdministrativeCostsAdmin(admin.ModelAdmin):
    list_display = ('accounting', 'datetime',)


admin.site.register(Expense, ExpenseAdmin)
admin.site.register(ActionLogs, ActionLogsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ExpenseUser)
admin.site.register(AdministrativeCosts, AdministrativeCostsAdmin)
