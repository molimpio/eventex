# Generated by Django 4.1.1 on 2022-10-17 17:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_alter_subscription_cpf_alter_subscription_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url_identity',
            field=models.UUIDField(default=uuid.UUID('e73022aa-4f43-4d06-a602-4fa63331380f')),
        ),
    ]