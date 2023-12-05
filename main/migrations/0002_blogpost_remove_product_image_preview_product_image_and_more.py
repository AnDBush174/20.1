# Generated by Django 4.2.7 on 2023-12-04 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField()),
                ('preview', models.ImageField(upload_to='blog_previews/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_published', models.BooleanField(default=False)),
                ('views_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_preview',
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(default='default.png', upload_to='products/'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='inn',
            field=models.CharField(max_length=15, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_modification',
            field=models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения'),
        ),
    ]
