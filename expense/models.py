from django.db import models
from django.utils import timezone


class ExpenseUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name} Phone: {self.phone}"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"Category Name: {self.name}"

class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10 ,decimal_places=2, null=True)
    date = models.DateTimeField(auto_now=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Description: {self.description}, Category: {self.category}"


class ActionLogs(models.Model):
    method = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    endpoint = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"DateTime: {self.datetime}, Method: {self.method}, Status: {self.status}"