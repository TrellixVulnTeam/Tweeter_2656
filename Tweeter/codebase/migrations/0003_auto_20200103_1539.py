# Generated by Django 3.0 on 2020-01-03 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codebase', '0002_auto_20200102_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='dob',
            field=models.DateField(blank=True),
        ),
    ]
