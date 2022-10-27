from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class ContactModelTest(TestCase):
    def setUp(self) -> None:
        self.speaker = Speaker.objects.create(
            name='Moises Olimpio',
            slug='moises-olimpio',
            photo='https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia-exp1.licdn.com%2Fdms%2Fimage%2FC4E03AQGJcQ2WBuRg7w%2Fprofile-displayphoto-shrink_200_200%2F0%2F1517059515095%3Fe%3D2147483647%26v%3Dbeta%26t%3DHZzWZh8EsO9kqUZypYAeVmAD64-OJ7DsGv0Ifa7b1d0&imgrefurl=https%3A%2F%2Fbr.linkedin.com%2Fin%2Fmoises-olimpio&tbnid=-iPbvHwZvZzhGM&vet=12ahUKEwjFmqj71On6AhUSCbkGHTzfBCIQMygCegQIARBA..i&docid=y2JBUpBaiLyT1M&w=200&h=200&itg=1&q=moises%20olimpio&ved=2ahUKEwjFmqj71On6AhUSCbkGHTzfBCIQMygCegQIARBA'
        )

    def test_email(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.EMAIL, value='moisesolimpiofilho@gmail.com')
        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        Contact.objects.create(speaker=self.speaker, kind=Contact.PHONE, value='19993934567')
        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E ou P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(speaker=self.speaker, kind=Contact.EMAIL, value='moisesolimpiofilho@gmail.com')
        self.assertEqual('moisesolimpiofilho@gmail.com', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self) -> None:
        s = Speaker.objects.create(
            name='Moises Olimpio',
            slug='moises-olimpio',
            photo='https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia-exp1.licdn.com%2Fdms%2Fimage%2FC4E03AQGJcQ2WBuRg7w%2Fprofile-displayphoto-shrink_200_200%2F0%2F1517059515095%3Fe%3D2147483647%26v%3Dbeta%26t%3DHZzWZh8EsO9kqUZypYAeVmAD64-OJ7DsGv0Ifa7b1d0&imgrefurl=https%3A%2F%2Fbr.linkedin.com%2Fin%2Fmoises-olimpio&tbnid=-iPbvHwZvZzhGM&vet=12ahUKEwjFmqj71On6AhUSCbkGHTzfBCIQMygCegQIARBA..i&docid=y2JBUpBaiLyT1M&w=200&h=200&itg=1&q=moises%20olimpio&ved=2ahUKEwjFmqj71On6AhUSCbkGHTzfBCIQMygCegQIARBA'
        )
        s.contact_set.create(kind=Contact.EMAIL, value='moisesolimpiofilho@gmail.com')
        s.contact_set.create(kind=Contact.PHONE, value='11-12341234')

    def test_emails(self):
        qs = Contact.objects.emails()
        expected = ['moisesolimpiofilho@gmail.com']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['11-12341234']
        self.assertQuerysetEqual(qs, expected, lambda o: o.value)
