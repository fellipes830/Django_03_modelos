# Generated by Django 2.1.3 on 2018-12-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20181201_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemagenda',
            name='data',
            field=models.DateField(),
        ),
    ]
