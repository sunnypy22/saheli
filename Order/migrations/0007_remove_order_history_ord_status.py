# Generated by Django 3.2.4 on 2021-07-28 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0006_auto_20210728_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_history',
            name='ord_status',
        ),
    ]
