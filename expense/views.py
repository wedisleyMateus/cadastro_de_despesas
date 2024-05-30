from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ExpenseUser, Expense, ActionLogs, Category
from .serializer import ExpenseUserSerializer, ExpenseSerializer, CategorySerializer

def home(request):
    return HttpResponse("Bem Vindo")


def save_action_log(method, status, endpoint):
    log = ActionLogs()
    log.method = method
    log.status = status
    log.endpoint = endpoint
    log.save()
        

class ExpenseUserList(APIView):

    def get(self, request, format=None):
        user = ExpenseUser.objects.all()
        serializer = ExpenseUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenseUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExpenseUserDetail(APIView):

    def get_object(self, pk):
        try:
            return ExpenseUser.objects.get(pk=pk)
        except ExpenseUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        user = ExpenseUser.get_object(pk)
        serializer = ExpenseUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = ExpenseUser.get_object(pk)
        serializer = ExpenseUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        user = ExpenseUser.get_objetc(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ExpenseList(LoginRequiredMixin, APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        save_action_log(request.method, status=status.HTTP_200_OK, endpoint=request.path)
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        expense = Expense.objects.all()
        serializer = ExpenseSerializer(expense, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseDetail(LoginRequiredMixin, APIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        save_action_log(request.method, status=status.HTTP_200_OK, endpoint=request.path)
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, pk):
        try:
            return Expense.objects.get(pk=pk)
        except Expense.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        expense = self.get_object(pk)
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        expense = self.get_object(pk)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryList(LoginRequiredMixin, APIView):

    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class CategoryDatail(LoginRequiredMixin, APIView):

    def get_objects(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        category = self.get_objects(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_objects(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        category = self.get_objects(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)