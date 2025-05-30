# Generated by Django 5.1.1 on 2025-05-25 12:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UserLogApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(verbose_name='Название задачи')),
                ('deadline', models.DateTimeField(verbose_name='Срок')),
                ('copmpleted', models.BooleanField(verbose_name='Выполнено')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='UserLogApp.user', verbose_name='Пользователь')),
            ],
        ),
    ]
