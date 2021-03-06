# Generated by Django 4.0.3 on 2022-03-24 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schedule", "0004_scheduling_confirmed_alter_scheduling_canceled_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="scheduling",
            name="states",
            field=models.CharField(
                choices=[
                    ("NCNF", "Not confirmed"),
                    ("CONF", "Confirmed"),
                    ("EXEC", "Executed"),
                    ("CANC", "Canceled"),
                ],
                default="NCNF",
                max_length=4,
                verbose_name="Estados do elemento",
            ),
        ),
    ]
