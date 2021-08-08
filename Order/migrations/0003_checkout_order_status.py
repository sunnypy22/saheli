# Generated by Django 3.2.4 on 2021-08-08 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0002_auto_20210807_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='order_status',
            field=models.CharField(blank=True, choices=[('Prepare To Dispatch', 'Prepare To Dispatch'), ('Dispatch', 'Dispatch'), ('Received', 'Received')], default=('Prepare To Dispatch', 'Prepare To Dispatch'), max_length=50, null=True),
        ),
    ]
