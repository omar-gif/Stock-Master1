# Generated by Django 4.1.2 on 2023-05-11 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0065_autoorderinvoice'),
    ]

    operations = [
        migrations.AddField(
            model_name='autoorderinvoice',
            name='CatNumber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.reagentqty'),
        ),
    ]