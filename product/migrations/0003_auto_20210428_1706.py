# Generated by Django 3.2 on 2021-04-28 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_victim'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='is_active',
            new_name='is_available',
        ),
        migrations.RemoveField(
            model_name='product',
            name='in_stock',
        ),
    ]
