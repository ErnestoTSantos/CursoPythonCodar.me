# Generated by Django 4.0.2 on 2022-02-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_event_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.IntegerField(default=0),
        ),
    ]
