# Generated by Django 4.1.2 on 2023-03-05 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0010_undertest_lotnum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='undertest',
            name='LotNum',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
