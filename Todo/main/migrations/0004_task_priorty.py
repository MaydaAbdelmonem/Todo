# Generated by Django 5.1 on 2024-09-02 00:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_comment_status_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priorty',
            field=models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
