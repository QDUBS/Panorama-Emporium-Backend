# Generated by Django 4.1.5 on 2023-03-30 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_remove_service_price_bookings_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='slug',
            field=models.SlugField(default='winner', max_length=100),
            preserve_default=False,
        ),
    ]