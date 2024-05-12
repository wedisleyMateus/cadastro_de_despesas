from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete

class BankingAssociation(models.Model):
    service = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=False)

    def __str__(self):
        return f"service: {self.service}, Value: {self.value}, Date: {self.date}"

class RevenueValue(models.Model):
    fixed_revenue = models.ForeignKey(BankingAssociation, 
                                      on_delete=models.CASCADE, null=True, blank=True)
    variable_revenue = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(auto_now=False)
    details = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"Fixed Revenue: {self.fixed_revenue}, Variable Revenue:{self.variable_revenue}, Date: {self.date}"

class NetRevenue(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.amount


@receiver([post_save, post_delete], sender=RevenueValue)
def update_net_revenue(sender, instance, **kwargs):
    created, net_revenue = NetRevenue.objects.get_or_create(pk=1)

    total_revenue = RevenueValue.objects.all().aggregate(n1=Sum('fixed_revenue__value'), n2=Sum('variable_revenue'))
    net_revenue = NetRevenue.objects.first()
    count = float(total_revenue['n1'] or 0) + float(total_revenue['n2'] or 0)
    net_revenue.amount = count
    net_revenue.save()
