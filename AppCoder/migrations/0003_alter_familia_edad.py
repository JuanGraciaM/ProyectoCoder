# Generated by Django 4.1 on 2022-08-17 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_familia_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familia',
            name='edad',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
