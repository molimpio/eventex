# Generated by Django 4.1.1 on 2022-10-06 11:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'ordering': ('-created_at',), 'verbose_name': 'inscrição', 'verbose_name_plural': 'inscrições'},
        ),
        migrations.AddField(
            model_name='subscription',
            name='url_identity',
            field=models.UUIDField(default=uuid.UUID('c8e19abe-266e-40cd-9488-6a0d478daf9e')),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='criado em'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='name',
            field=models.CharField(max_length=100, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='telefone'),
        ),
    ]
