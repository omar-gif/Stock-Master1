# Generated by Django 4.1.2 on 2023-05-12 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0068_alter_autoorderinvoice_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoconfdata',
            name='excfile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.excelfile'),
        ),
    ]
