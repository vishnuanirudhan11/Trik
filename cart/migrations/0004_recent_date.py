# Generated by Django 4.0.3 on 2022-05-27 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_remove_recent_productid_alter_recent_userid'),
    ]

    operations = [
        migrations.AddField(
            model_name='recent',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
