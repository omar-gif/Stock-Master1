# Generated by Django 4.1.2 on 2023-10-30 13:14

import boards.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0089_remove_jobsheet_nameofitem_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospitalsanalyzers',
            name='Counter',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hospitalsanalyzers',
            name='PM',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='hospitalsanalyzers',
            name='Software',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(null=True, upload_to=boards.models.path_and_renameListing5),
        ),
    ]
