from rest_framework import serializers
from .models import Expense, ActionLogs

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'