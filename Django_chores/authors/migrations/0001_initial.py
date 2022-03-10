# Generated by Django 4.0.2 on 2022-03-01 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='Primeiro nome')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='Sobrenome')),
                ('age', models.IntegerField(verbose_name='Idade')),
            ],
        ),
    ]