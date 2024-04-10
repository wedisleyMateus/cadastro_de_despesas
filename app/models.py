from django.db import models
from django.utils import timezone


class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10 ,decimal_places=2, null=True)
    date = models.DateTimeField(auto_now=False)
    category = models.CharField(max_length=30)

    def __str__(self):
        return f"Description: {self.description}, Category: {self.category}"


class ActionLogs(models.Model):
    method = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    endpoint = models.CharField(max_length=30)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"DateTime: {self.datetime}, Method: {self.method}, Status: {self.status}"