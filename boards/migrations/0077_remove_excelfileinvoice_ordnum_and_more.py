# Generated by Django 4.1.2 on 2023-05-19 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0076_excelfileinvoice_ordnum_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excelfileinvoice',
            name='ordnum',
        ),
        migrations.AlterField(
            model_name='excelfileinvoice',
            name='ordinv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.oradercreation'),
        ),
    ]
