# Generated by Django 4.0.3 on 2022-05-16 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='products',
            new_name='productstable',
        ),
    ]