# Generated by Django 4.1.2 on 2023-05-01 10:17

import boards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0054_alter_excelfile_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excelfile',
            name='file',
            field=models.FileField(upload_to=boards.models.path_and_renameListing),
        ),
    ]