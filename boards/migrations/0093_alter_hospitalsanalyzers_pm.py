# Generated by Django 4.1.2 on 2023-11-08 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0092_hospitalsanalyzers_stab_hospitalsanalyzers_ups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitalsanalyzers',
            name='PM',
            field=models.DateField(max_length=250, null=True),
        ),
    ]
