# Generated by Django 3.2.4 on 2021-08-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='ammount',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='product',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
