from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Expense, ActionLogs
from .serializer import ExpenseSerializer

def home(request):
    return HttpResponse("Bem Vindo")


def save_action_log(method, status, endpoint):
    log = ActionLogs()
    log.method = method
    log.status = status
    log.endpoint = endpoint
    log.save()
        
    
@api_view(['GET', 'POST']) #Parametro de comando HTTP e que devera responder
def expense_list(request): #Minha função de trazer todos meus opjetos e criar um novo
    save_action_log(request.method, status=status.HTTP_200_OK, endpoint=request.path)
    if request.method == 'GET': # se minha requisição for do metodo GET faça algo para mim
        expense = Expense.objects.all() # variavel que recebe todos os meus objetos do meu model
        serializer = ExpenseSerializer(expense, many=True) # variavel que recebe meu serializer
        return Response(serializer.data) # retorna minha resposta que trara da minha variavel o .data e os dados dela
    elif request.method == 'POST':
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) # retorna um status ja pre formatado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def expense_detail(request, pk):
    try:
        expense = Expense.objects.get(pk=pk)
    except Expense.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ExpenseSerializer(expense, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)