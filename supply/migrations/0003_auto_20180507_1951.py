# Generated by Django 2.0.4 on 2018-05-07 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0002_auto_20180503_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='supply.ServiceArea'),
        ),
    ]
