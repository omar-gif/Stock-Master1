# Generated by Django 4.1.2 on 2023-05-12 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0069_autoconfdata_excfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='Cal',
        ),
    ]