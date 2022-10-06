from datetime import datetime
from uuid import uuid4

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription(
            name='Moises Olimpio',
            cpf='12345678901',
            email='moisesolimpiofilho@gmail.com',
            phone='19-991231234'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscription must have an auto created_at attribute"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Moises Olimpio', str(self.obj))
