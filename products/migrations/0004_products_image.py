# Generated by Django 3.0.2 on 2020-02-03 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200203_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='static/images/The_Fresh_Market_logo.svg', upload_to='images/'),
        ),
    ]
