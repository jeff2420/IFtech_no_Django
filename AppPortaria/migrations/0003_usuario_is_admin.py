# Generated by Django 5.0.3 on 2024-08-01 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPortaria', '0002_alter_usuario_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
