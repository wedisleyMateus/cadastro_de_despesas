from django.contrib import admin
from .models import User, Category


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)

