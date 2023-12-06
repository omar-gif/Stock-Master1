# Generated by Django 4.1.2 on 2023-04-09 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0027_alter_parametername_slidenumber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parametername',
            name='CatNumber',
        ),
        migrations.RemoveField(
            model_name='parametername',
            name='slideNumber',
        ),
        migrations.CreateModel(
            name='ReagentQTY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CatNumber', models.CharField(default=None, max_length=255, null=True)),
                ('slideNumber', models.IntegerField(default=None, null=True)),
                ('Item_Model_compName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyname')),
                ('Item_Model_compUnit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyunits')),
                ('ParName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.parametername')),
            ],
        ),
    ]