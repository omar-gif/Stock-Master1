# Generated by Django 4.1.2 on 2023-03-30 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0018_oradercreation_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='parametername',
            name='Item_Model_compName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyname'),
        ),
        migrations.AddField(
            model_name='parametername',
            name='Item_Model_compUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyunits'),
        ),
    ]
