# Generated by Django 4.1.2 on 2023-05-01 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0056_autoconfdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoconfdata',
            name='matrial',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]