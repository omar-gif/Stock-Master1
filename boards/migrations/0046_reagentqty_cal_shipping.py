# Generated by Django 4.1.2 on 2023-04-22 23:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0045_alter_orderinvoice_orderconfermation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reagentqty',
            name='Cal',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PO', models.CharField(default=None, max_length=255, null=True)),
                ('ImportApproval', models.CharField(default=None, max_length=255, null=True)),
                ('OkToShip', models.CharField(default=None, max_length=255, null=True)),
                ('ShippingDate', models.DateField(default=None, max_length=255, null=True)),
                ('ShippingCond', models.CharField(default=None, max_length=255, null=True)),
                ('ArrivalDate', models.DateField(default=None, max_length=255, null=True)),
                ('EDADate', models.DateField(default=None, max_length=255, null=True)),
                ('TechDate', models.DateField(default=None, max_length=255, null=True)),
                ('EDAReleaseDate', models.DateField(default=None, max_length=255, null=True)),
                ('Cal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.reagentqty')),
                ('InvNumber', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.orderinvoice')),
                ('Item_Model_compName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyname')),
                ('Item_Model_compUnit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyunits')),
            ],
        ),
    ]