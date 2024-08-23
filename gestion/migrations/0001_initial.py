# Generated by Django 5.1 on 2024-08-23 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
                ('estado', models.CharField(choices=[('terminado', 'tarea completa'), ('incompleto', 'tarea pendiente')], default='incompleto', max_length=100)),
            ],
        ),
    ]
