# Generated by Django 3.2.4 on 2021-07-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_remove_order_history_ord_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='billing_company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='billing_phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='billing_postcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='order_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='checkout',
            name='order_comments',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
