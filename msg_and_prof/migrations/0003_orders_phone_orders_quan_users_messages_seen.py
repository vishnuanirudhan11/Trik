# Generated by Django 4.0.3 on 2022-05-25 09:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('msg_and_prof', '0002_orders_cancel_orders_done_date_orders_ordered_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='quan',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seen', models.BooleanField(default=False)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='messages',
            name='seen',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='msg_and_prof.users'),
        ),
    ]
