# Generated by Django 4.1.2 on 2022-11-18 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mayphat", "0020_order_detail_qty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order", name="full_name", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="order",
            name="payment_code",
            field=models.IntegerField(default=0),
        ),
    ]
