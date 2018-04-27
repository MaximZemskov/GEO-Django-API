# Generated by Django 2.0.4 on 2018-04-23 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0004_servicearea_poly'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='servicearea',
            options={'verbose_name': 'Сервисная зона', 'verbose_name_plural': 'Сервисные зоны'},
        ),
        migrations.AlterModelOptions(
            name='supplier',
            options={'verbose_name': 'Поставщик', 'verbose_name_plural': 'Поставщики'},
        ),
        migrations.RemoveField(
            model_name='service',
            name='service',
        ),
        migrations.AddField(
            model_name='service',
            name='title',
            field=models.CharField(default='Услуга', max_length=120, verbose_name='Название услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.CharField(max_length=60, verbose_name='Цена услуги'),
        ),
        migrations.AlterField(
            model_name='service',
            name='service_area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='services', to='supply.ServiceArea'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='title',
            field=models.CharField(max_length=60, verbose_name='Название'),
        ),
    ]