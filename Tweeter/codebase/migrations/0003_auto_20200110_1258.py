# Generated by Django 3.0 on 2020-01-10 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('codebase', '0002_edithistory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='edithistory',
            options={'verbose_name_plural': 'Edit Histories'},
        ),
        migrations.AlterField(
            model_name='edithistory',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='codebase.Post'),
        ),
    ]
