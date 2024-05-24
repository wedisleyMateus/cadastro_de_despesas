from django.contrib import admin
from .models import User, Category
from .models import Recurrence, Contract
from .models import RecipeCategory, Recipe
from .models import PaymentMethod,  ContractRecipe


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class RecurrenceAdmin(admin.ModelAdmin):
    list_display = ['type']


class ContractAdmin(admin.ModelAdmin):
    list_display = ['get_user', 'name', 'value']

    def get_user(self, obj):
        return obj.user.name
    get_user.short_description = 'User'
    get_user.admin_order_field = 'user__name'


class RecipeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['recipe_category', 'user', 'value']


class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['name']


class ContractRecipeAdmin(admin.ModelAdmin):
    list_display = ['get_contract', 'get_recipe', 'get_payment_form']

    def get_contract(self, obj):
        return obj.contract.name
    get_contract.short_description = 'Contract'
    get_contract.admin_order_field = 'contract__name'

    def get_recipe(self, obj):
        return obj.recipe.value
    get_recipe.short_description = 'Recipe'
    get_recipe.admin_order_field = 'recipe__value'

    def get_payment_form(self, obj):
        return obj.payment_form.name
    get_payment_form.short_description = 'Payment Form'
    get_payment_form.admin_order_field = 'payment_form__name'


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Recurrence, RecurrenceAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(RecipeCategory, RecipeCategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(PaymentMethod, PaymentMethodAdmin)
admin.site.register(ContractRecipe, ContractRecipeAdmin)
