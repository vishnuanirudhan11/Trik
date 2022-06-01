# Generated by Django 4.0.3 on 2022-05-23 08:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0002_alter_cart_id_session_alter_cart_id_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('home', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart_id')),
            ],
        ),
    ]
