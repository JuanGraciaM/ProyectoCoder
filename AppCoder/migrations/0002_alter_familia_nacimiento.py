# Generated by Django 4.1 on 2022-08-17 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='nacimiento',
            field=models.DateField(),
        ),
    ]
