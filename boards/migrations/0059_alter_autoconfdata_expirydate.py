# Generated by Django 4.1.2 on 2023-05-02 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0058_alter_elementconfermation_slidesqty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autoconfdata',
            name='ExpiryDate',
            field=models.DateField(default=None, max_length=255, null=True),
        ),
    ]
