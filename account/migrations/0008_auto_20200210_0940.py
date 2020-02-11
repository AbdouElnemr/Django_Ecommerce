# Generated by Django 3.0.2 on 2020-02-10 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('account', '0007_auto_20200209_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='orders',
            field=models.ManyToManyField(blank=True, related_name='profile_orders', to='orders.Order'),
        ),
    ]
