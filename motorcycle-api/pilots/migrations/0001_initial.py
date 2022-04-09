# Generated by Django 4.0.3 on 2022-03-20 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pilot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=50, unique=True, verbose_name="Nome do piloto"
                    ),
                ),
                ("age", models.IntegerField(verbose_name="Idade")),
                (
                    "number",
                    models.IntegerField(unique=True, verbose_name="Número do piloto"),
                ),
                (
                    "automaker",
                    models.CharField(max_length=50, verbose_name="Montadora"),
                ),
                (
                    "championships_won",
                    models.IntegerField(verbose_name="Campeonatos vencidos"),
                ),
                (
                    "retired",
                    models.BooleanField(default=False, verbose_name="Está aposentado"),
                ),
            ],
            options={
                "verbose_name": "Pilot",
                "verbose_name_plural": "Pilots",
            },
        ),
    ]
