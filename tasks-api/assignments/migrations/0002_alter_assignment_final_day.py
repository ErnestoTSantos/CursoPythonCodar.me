# Generated by Django 4.0.3 on 2022-04-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("assignments", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignment",
            name="final_day",
            field=models.DateField(
                blank=True, null=True, verbose_name="Dia da finalização"
            ),
        ),
    ]
