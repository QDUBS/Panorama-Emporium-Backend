# Generated by Django 4.1.5 on 2023-02-03 13:47

from django.db import migrations, models
import django.db.models.deletion
import publik.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.CharField(default=publik.utils.custom_id, editable=False, max_length=30, primary_key=True, serialize=False, unique=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
            options={
                'verbose_name_plural': 'Order Items Details',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.CharField(default=publik.utils.custom_id, editable=False, max_length=30, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField()),
                ('discount', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(default='', upload_to='images')),
                ('thumbnail', models.ImageField(blank=True, default='', null=True, upload_to='thumbnails')),
                ('percent', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(max_length=400)),
                ('rating', models.IntegerField(blank=True, default=1, null=True)),
                ('slug', models.SlugField(blank=True, default='', null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('available', models.BooleanField(default=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
    ]