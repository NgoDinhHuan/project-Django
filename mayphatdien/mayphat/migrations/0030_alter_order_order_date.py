# Generated by Django 4.1.2 on 2022-11-28 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mayphat", "0029_order_order_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
