# Generated by Django 5.0.2 on 2024-03-16 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('apellido', models.CharField(max_length=30, null=True)),
                ('telefono', models.IntegerField()),
                ('mail', models.EmailField(max_length=40)),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='contac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.CharField(max_length=40)),
                ('tareas', models.CharField(max_length=40)),
                ('id_empleado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contac.empleado')),
            ],
        ),
    ]