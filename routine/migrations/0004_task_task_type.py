# Generated by Django 4.1.7 on 2023-03-08 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routine', '0003_task_task_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_type',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
