from .models import User
from .models import Recurrence
from .models import Contract
from .models import RecipeCategory
from .models import Recipe
from .models import PaymentMethod
from .models import ContractRecipe

from .serializer import UserSerializer
from .serializer import RecurrenceSerializer
from .serializer import ContractSerializer
from .serializer import RecipeCategorySerializer
from .serializer import RecipeSerializer
from .serializer import PaymentMethodSerializer
from .serializer import ContractRecipeSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserList(APIView):

    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecurrenceList(APIView):

    def get(self, request, format=None):
        recurrence = Recurrence.objects.all()
        serializer = RecurrenceSerializer(recurrence)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecurrenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecurrenceDetail(APIView):

    def get_object(self, pk):
        try:
            return Recurrence.objects.get(pk=pk)
        except Recurrence.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        recurrence = self.get_object(pk)
        serializer = RecurrenceSerializer(recurrence)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recurrence = self.get_object(pk)
        serializer = RecurrenceSerializer(recurrence, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recurrence = self.get_object(pk)
        recurrence.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContractList(APIView):

    def get(self, request, format=None):
        contract = Contract.objects.all()
        serializer = ContractSerializer(contract)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContractSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractDetail(APIView):

    def get_object(self, pk):
        try:
            return Contract.objects.get(pk=pk)
        except Contract.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        contract = self.get_object(pk)
        serializer = ContractSerializer(contract)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contract = self.get_object(pk)
        serializer = ContractSerializer(contract, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contract = self.get_object(pk)
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeCategoryList(APIView):

    def get(self, request, format=None):
        recipecategory = RecipeCategory.objects.all()
        serializer = RecipeCategorySerializer(recipecategory)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeCategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return RecipeCategory.objects.get(pk=pk)
        except RecipeCategory.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        recipecategory = self.get_object(pk)
        serializer = RecipeCategorySerializer(recipecategory)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipecategory = self.get_object(pk)
        serializer = RecipeCategorySerializer(recipecategory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipecategory = self.get_object(pk)
        recipecategory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecipeList(APIView):

    def get(self, request, format=None):
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PaymentList(APIView):

    def get(self, request, format=None):
        payment = PaymentMethod.objects.all()
        serializer = PaymentMethodSerializer(payment)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PaymentMethodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentDetail(APIView):

    def get_object(self, pk):
        try:
            return PaymentMethod.objects.get(pk=pk)
        except PaymentMethod.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        payment = self.get_object(pk)
        serializer = PaymentMethodSerializer(payment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        payment = self.get_object(pk)
        serializer = PaymentMethodSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        payment = self.get_object(pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContractRecipeList(APIView):

    def get(self, request, format=None):
        contract_recipe = ContractRecipe.objects.all()
        serializer = ContractRecipeSerializer(contract_recipe)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContractRecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContractRecipeDetail(APIView):

    def get_object(self, pk):
        try:
            return ContractRecipe.objects.get(pk=pk)
        except ContractRecipe.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        contract_recipe = self.get_object(pk)
        serializer = ContractRecipeSerializer(contract_recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        contract_recipe = self.get_object(pk)
        serializer = ContractRecipeSerializer(contract_recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        contract_recipe = self.get_object(pk)
        contract_recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
