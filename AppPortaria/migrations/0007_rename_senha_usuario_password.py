# Generated by Django 5.0.3 on 2024-08-09 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppPortaria', '0006_remove_movimento_cor_remove_movimento_modelo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='senha',
            new_name='password',
        ),
    ]
