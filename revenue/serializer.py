from rest_framework import serializers
from .models import BankingAssociation, RevenueValue

class BankingAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankingAssociation
        fields = '__all__'

class RevenueValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = RevenueValue
        fields = '__all__'