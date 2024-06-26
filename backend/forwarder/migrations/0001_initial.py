# Generated by Django 4.2.6 on 2024-04-09 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Forwarder',
            fields=[
                ('id_forwarder', models.AutoField(primary_key=True, serialize=False)),
                ('ruc', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qoutation',
            fields=[
                ('id_qoutation', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=255)),
                ('supplier', models.CharField(max_length=255)),
                ('incoterm', models.CharField(max_length=25)),
                ('portOrigin', models.CharField(max_length=55)),
                ('portDestination', models.CharField(max_length=55)),
                ('transitDays', models.IntegerField(default=0)),
                ('gOrigin', models.FloatField(default=0)),
                ('currencyGo', models.CharField(max_length=3)),
                ('freight', models.FloatField(default=0)),
                ('currencyFreight', models.CharField(max_length=3)),
                ('localExpenses', models.FloatField(default=0)),
                ('freeDays', models.IntegerField(default=0)),
                ('offerDays', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('forwarder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forwarder.forwarder')),
            ],
        ),
    ]
