from django.contrib import admin
from .models import User, Category
from .models import Recurrence, Contract
from .models import RecipeCategory, Recipe


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class RecurrenceAdmin(admin.ModelAdmin):
    list_display = ['type']


class ContractAdmin(admin.ModelAdmin):
    list_display = ['name', 'value']


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['Value']


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recurrence, RecurrenceAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)

