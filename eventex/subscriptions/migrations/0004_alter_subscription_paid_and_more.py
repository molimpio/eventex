# Generated by Django 4.1.1 on 2022-10-07 10:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscription_paid_alter_subscription_url_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='paid',
            field=models.BooleanField(default=False, verbose_name='pago'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='url_identity',
            field=models.UUIDField(default=uuid.UUID('05314e96-9cad-43fb-9679-ac5fce5ccba9')),
        ),
    ]
