# Generated by Django 4.1.2 on 2023-11-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0095_workflowline'),
    ]

    operations = [
        migrations.AddField(
            model_name='workflowline',
            name='date',
            field=models.DateField(max_length=50, null=True),
        ),
    ]
