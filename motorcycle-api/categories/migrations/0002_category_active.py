# Generated by Django 4.0.3 on 2022-03-21 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Categoria ativa'),
        ),
    ]