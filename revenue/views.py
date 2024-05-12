from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import BankingAssociation, RevenueValue
from .serializer import (
    BankingAssociationSerializer, 
    RevenueValueSerializer
)

@api_view(['GET', 'POST'])
def associations_list(request):
    if request.method == 'GET':
        association = BankingAssociation.objects.all()
        serializer = BankingAssociationSerializer(association, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BankingAssociationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
def association_detail(request, pk):
    try:
        association = BankingAssociation.objects.get(pk=pk)
    except BankingAssociation.DoesNotExist:
        return Response(statys=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'GET':
        serializer = BankingAssociationSerializer(association)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BankingAssociationSerializer(association, data=serializer.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        association.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)