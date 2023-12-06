# Generated by Django 4.1.2 on 2023-10-27 14:43

import boards.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0087_alter_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobSheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfJobSheet', models.DateField(max_length=50, null=True)),
                ('Note', models.CharField(max_length=255, null=True)),
                ('cost', models.IntegerField(default=0, null=True)),
                ('Hospital', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.hospitalsanalyzers')),
                ('Item_Model_compName', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyname')),
                ('Item_Model_compUnit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.companyunits')),
                ('Item_Model_workFlow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.workflow')),
                ('mainUser', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('nameOfItem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.iteminput')),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(null=True, upload_to=boards.models.path_and_renameListing5),
        ),
        migrations.CreateModel(
            name='JobSheetImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(null=True, upload_to=boards.models.path_and_renameListing5)),
                ('Inpu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.jobsheet')),
            ],
        ),
        migrations.AddField(
            model_name='assembledstore',
            name='JobSheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.jobsheet'),
        ),
    ]