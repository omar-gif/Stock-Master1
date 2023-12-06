# Generated by Django 4.1.2 on 2023-04-14 21:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0037_alter_oradercreation_dat'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat', models.CharField(default=None, max_length=255, null=True)),
                ('Price', models.IntegerField(default=None, null=True)),
                ('orderNum', models.CharField(default=None, max_length=255, null=True)),
                ('ElementName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.parametername')),
                ('Item_Model_compName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyname')),
                ('Item_Model_compUnit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyunits')),
            ],
        ),
    ]
