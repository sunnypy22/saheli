# Generated by Django 3.2.4 on 2021-08-01 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_alter_product_pro_cat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_cat_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pro_cat_name', to='Product.category'),
        ),
    ]