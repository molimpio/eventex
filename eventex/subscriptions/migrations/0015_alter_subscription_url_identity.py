# Generated by Django 4.1.2 on 2022-11-03 17:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_alter_subscription_url_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='url_identity',
            field=models.UUIDField(default=uuid.UUID('91595872-7923-49b8-8733-57a25792199b')),
        ),
    ]
