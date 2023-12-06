# Generated by Django 4.1.2 on 2023-05-11 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0064_reagentqty_shippindcond'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoOrderInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dat', models.CharField(default=None, max_length=255, null=True)),
                ('Price', models.IntegerField(default=None, null=True)),
                ('orderNum', models.CharField(default=None, max_length=255, null=True)),
                ('InvoiceNumber', models.CharField(default=None, max_length=255, null=True)),
                ('orderConfermation', models.CharField(default=None, max_length=255, null=True)),
                ('Item_Model_compName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyname')),
                ('Item_Model_compUnit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyunits')),
            ],
        ),
    ]
