from django.test import TestCase
from revenue.models import BankingAssociation
from django.utils import timezone

class RevenueTestCase(TestCase):
    def setUp(self):
        BankingAssociation.objects.create(service="APEX", value="100", date=timezone.now())
        BankingAssociation.objects.create(service="Veneza", value="200", date=timezone.now())

    def test_all_banking(self):
        queryset = BankingAssociation.objects.all()
        print("All Banking:", queryset)
        assert queryset

    def test_first_banking(self):
        queryset = BankingAssociation.objects.first()
        print("First Banking:", queryset)
        assert queryset
