# Generated by Django 4.1.2 on 2023-04-13 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0031_elementconfermation_catnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oradercreation',
            name='dat',
            field=models.DateField(default=None, max_length=255, null=True),
        ),
    ]
