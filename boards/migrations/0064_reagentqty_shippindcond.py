# Generated by Django 4.1.2 on 2023-05-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0063_elementconfermation_batchnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='reagentqty',
            name='ShippindCond',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
