import uuid

from django.shortcuts import resolve_url as r
from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription.objects.create(
            name='Moises Olimpio',
            cpf='12345678901',
            email='moisesolimpiofilho@gmail.com',
            phone='1999912234567'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.url_identity))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.email, self.obj.cpf, self.obj.phone)

        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get(r('subscriptions:detail', uuid.uuid4()))
        self.assertEqual(404, resp.status_code)
