# Generated by Django 4.1.2 on 2023-04-22 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0047_calibrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shipping',
            name='Cal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.calibrator'),
        ),
    ]