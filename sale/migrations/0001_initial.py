# Generated by Django 5.0.1 on 2024-05-22 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parameter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('OS', models.CharField(max_length=50)),
                ('count', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('info', models.TextField()),
                ('CPU', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parameter.cpu')),
                ('GPU', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parameter.gpu')),
                ('RAM', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='parameter.ram')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sale.category')),
            ],
        ),
    ]
