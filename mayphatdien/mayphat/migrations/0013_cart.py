# Generated by Django 4.0.6 on 2022-11-03 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayphat', '0012_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_id', models.IntegerField(blank=True, max_length=20)),
            ],
        ),
    ]
