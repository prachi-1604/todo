# Generated by Django 4.1.13 on 2024-03-06 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_alter_todo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
