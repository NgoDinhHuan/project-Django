# Generated by Django 4.1.2 on 2022-11-28 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mayphat", "0030_alter_order_order_date"),
    ]

    operations = [
        migrations.RemoveField(model_name="order", name="order_date",),
    ]
