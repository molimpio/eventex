from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Moises Olimpio', cpf='12345678901',
                    email='moisesolimpiofilho@gmail.com', phone='1999912234567')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'olimpiodev@olimpiodev.kinghost.net'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['olimpiodev@olimpiodev.kinghost.net', 'moisesolimpiofilho@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Moises Olimpio',
            '12345678901',
            'moisesolimpiofilho@gmail.com',
            '1999912234567'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
