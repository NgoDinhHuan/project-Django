# Generated by Django 4.0.6 on 2022-09-21 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayphat', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='status',
            field=models.CharField(choices=[('Slide', 'Slide'), ('Bander', 'Bander')], default='Slide', max_length=15),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image_slide',
            field=models.ImageField(blank=True, upload_to='static/mayphat/slide-hinh/'),
        ),
    ]
