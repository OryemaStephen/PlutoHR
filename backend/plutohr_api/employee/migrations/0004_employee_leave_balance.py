# Generated by Django 5.0.6 on 2024-05-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_employee_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='leave_balance',
            field=models.IntegerField(blank=True, default=10),
        ),
    ]
