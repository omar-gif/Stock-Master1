# Generated by Django 4.1.2 on 2023-11-07 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0091_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalsanalyzers',
            name='Stab',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hospitalsanalyzers',
            name='Ups',
            field=models.CharField(max_length=250, null=True),
        ),
    ]