# Generated by Django 3.2 on 2022-11-27 13:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20221127_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': '价格必须在 0 和 999.99 之间'}}, help_text='最高 999.99 元', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='打折价格'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='product',
            name='regular_price',
            field=models.DecimalField(decimal_places=2, error_messages={'name': {'max_length': '价格必须在 0 和 999.99 之间'}}, help_text='最高 999.99 元', max_digits=5, validators=[django.core.validators.MinValueValidator(0)], verbose_name='平时价格'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
