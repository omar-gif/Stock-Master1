# Generated by Django 4.1.2 on 2023-04-10 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0029_elementcreation_catnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='elementcreation',
            name='SlidesQTY',
            field=models.IntegerField(default=None, null=True),
        ),
    ]