# Generated by Django 3.2.4 on 2021-07-28 16:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0005_order_history_order_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_history',
            name='ord_date',
        ),
        migrations.AddField(
            model_name='checkout',
            name='ord_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
