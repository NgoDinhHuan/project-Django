# Generated by Django 4.1.2 on 2022-11-16 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mayphat", "0019_order_country"),
    ]

    operations = [
        migrations.AddField(
            model_name="order_detail",
            name="qty",
            field=models.DecimalField(decimal_places=0, default=0, max_digits=12),
        ),
    ]
