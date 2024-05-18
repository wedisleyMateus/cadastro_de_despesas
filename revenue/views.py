from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import BankingAssociation, RevenueValue
from .serializer import (
    BankingAssociationSerializer, 
    RevenueValueSerializer
)

class AssociationsList(LoginRequiredMixin, APIView):

    def get(self, request, format=None):
        association = BankingAssociation.objects.all()
        serializer = BankingAssociationSerializer(association, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BankingAssociationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AssociationsDetail(LoginRequiredMixin, APIView):

    def get_object(self, pk):
        try:
            return BankingAssociation.objects.get(pk=pk)
        except BankingAssociation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        association = self.get_object(pk)
        serializer = BankingAssociationSerializer(association)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        association = self.get_object(pk)
        serializer = BankingAssociationSerializer(association, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        association = self.get_object(pk)
        association.dalete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RevenueList(LoginRequiredMixin, APIView):

    def get(self, request, format=None):
        revenue = RevenueValue.objects.all()
        serializer = RevenueValueSerializer(revenue, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RevenueValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class RevenueDetail(LoginRequiredMixin, APIView):

    def get_objects(self, pk):
        try:
            return RevenueValue.objects.get(pk=pk)
        except RevenueValue.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        revenue = self.get_objects(pk)
        serializer = RevenueValueSerializer(revenue)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        revenue = self.get_objects(pk)
        serializer = RevenueValueSerializer(revenue, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        revenue = self.get_objects(pk)
        revenue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
