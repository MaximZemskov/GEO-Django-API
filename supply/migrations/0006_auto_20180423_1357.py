# Generated by Django 2.0.4 on 2018-04-23 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0005_auto_20180423_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='title',
            field=models.CharField(max_length=120, verbose_name='Название услуги'),
        ),
    ]
