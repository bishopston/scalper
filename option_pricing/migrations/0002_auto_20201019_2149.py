# Generated by Django 3.1.2 on 2020-10-19 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option_pricing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='option',
            name='stock',
            field=models.FloatField(),
        ),
    ]
