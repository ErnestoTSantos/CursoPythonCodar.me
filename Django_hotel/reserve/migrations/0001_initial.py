# Generated by Django 4.0.3 on 2022-03-06 03:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accommodations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(verbose_name='Data do check-in')),
                ('check_out', models.DateField(verbose_name='Data do check-out')),
                ('person', models.CharField(max_length=50, verbose_name='Nome da reserva')),
                ('amount_people', models.IntegerField(verbose_name='Número de pessoas')),
                ('accommodation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodations.accommodation', verbose_name='Acomodação')),
            ],
        ),
    ]
