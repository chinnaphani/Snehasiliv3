# Generated by Django 3.0.7 on 2020-09-01 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberprofile', '0003_auto_20200901_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='monthsub_paiddate',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
