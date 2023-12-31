# Generated by Django 3.1.7 on 2021-11-20 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Rental', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=1500, null=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='car',
            name='consommation',
            field=models.IntegerField(verbose_name='Consommation (KM/L)'),
        ),
        migrations.AlterField(
            model_name='car',
            name='prix',
            field=models.IntegerField(verbose_name='Prix par jour(DH)'),
        ),
        migrations.AlterField(
            model_name='client',
            name='dateN',
            field=models.DateField(verbose_name='Date de naissance'),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateD', models.DateField(verbose_name='Check-In')),
                ('dateF', models.DateField(verbose_name='Check-Out')),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Rental.car', verbose_name='Rented Car')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reservation',
            },
        ),
    ]
