# Generated by Django 4.0.6 on 2022-11-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayphat', '0014_alter_cart_cart_id_alter_category_category_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Posttest',
        ),
        migrations.RemoveField(
            model_name='imageslide',
            name='image_name',
        ),
        migrations.AddField(
            model_name='imageslide',
            name='image_product',
            field=models.ImageField(blank=True, upload_to='static/mayphat/slide_hinh/'),
        ),
    ]
