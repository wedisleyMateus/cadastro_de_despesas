from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name} Phone: {self.phone}"

class Recurrence(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return f"Type of recurrence: {self.type}"

class Contract(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=timezone.now)
    term_date = models.DateField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    recurrence = models.ForeignKey(Recurrence, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Contract Name: {self.name}, Contractor: {self.user.name}, "
                f"Value: {self.value}")

class RecipeCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Category: {self.name}"

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    revenue_date = models.DateField(default=timezone.now)
    recipe_category = models.ForeignKey(RecipeCategory,
                                        on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    term_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return (f"Recipe Category: {self.recipe_category.name} - "
                f"{self.user.name} - {self.value}")

class PaymentMethod(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"Form of payment: {self.name}"

class ContractRecipe(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    paid = models.BinaryField()
    payment_form = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)

    def __str__(self):
        return (f"Contract: {self.contract.name} - {self.recipe.value} - "
                f"{self.payment_form.name}")
