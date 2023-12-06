# Generated by Django 4.1.2 on 2023-01-23 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assembledstore',
            name='Price',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='iteminput',
            name='cost',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.price'),
        ),
        migrations.AlterField(
            model_name='price',
            name='Price',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
