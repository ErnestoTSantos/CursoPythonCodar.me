# Generated by Django 4.0.2 on 2022-03-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0007_alter_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativa'),
        ),
    ]
