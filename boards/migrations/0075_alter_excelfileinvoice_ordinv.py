# Generated by Django 4.1.2 on 2023-05-19 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0074_excelfileinvoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfileinvoice',
            name='ordinv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.oradercreation'),
        ),
    ]
