# Generated by Django 4.1.2 on 2023-04-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0048_alter_shipping_cal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='ArrivalDate',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='EDADate',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='EDAReleaseDate',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='ShippingDate',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='TechDate',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
