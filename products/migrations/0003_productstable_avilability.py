# Generated by Django 4.0.3 on 2022-05-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_products_productstable'),
    ]

    operations = [
        migrations.AddField(
            model_name='productstable',
            name='avilability',
            field=models.BooleanField(default=True),
        ),
    ]
