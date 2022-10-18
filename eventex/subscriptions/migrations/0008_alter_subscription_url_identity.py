# Generated by Django 4.1.1 on 2022-10-18 11:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_alter_subscription_url_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url_identity',
            field=models.UUIDField(default=uuid.UUID('cba36073-0076-4c39-8466-eca159d5e773')),
        ),
    ]