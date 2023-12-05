# Generated by Django 4.2.7 on 2023-12-05 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_blogpost_remove_product_image_preview_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_preview',
            field=models.ImageField(default='default.png', upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]