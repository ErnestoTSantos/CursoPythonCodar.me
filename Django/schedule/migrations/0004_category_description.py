# Generated by Django 4.0.2 on 2022-02-28 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_event_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]