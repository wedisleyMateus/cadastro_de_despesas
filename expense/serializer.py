from rest_framework import serializers
from .models import Expense, Category, ExpenseUser, AdministrativeCosts


class ExpenseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseUser
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdministrativeCostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdministrativeCosts
        fields = '__all__'
