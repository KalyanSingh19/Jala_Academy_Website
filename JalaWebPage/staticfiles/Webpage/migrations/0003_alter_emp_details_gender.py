# Generated by Django 5.0.6 on 2024-08-15 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpage', '0002_skill_emp_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp_details',
            name='gender',
            field=models.CharField(max_length=100),
        ),
    ]
