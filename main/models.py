# main/models.py
from django.db import models
from datetime import datetime
from django.utils.text import slugify
from django.contrib.auth.models import Group, Permission


# Создаем группу модераторов
moderator_group, created = Group.objects.get_or_create(name='модератор')

# Находим необходимые разрешения
product_permissions = Permission.objects.filter(codename__in=['change_product', 'delete_product'])

# Добавляем разрешения в группу модераторов
for perm in product_permissions:
    moderator_group.permissions.add(perm)



class Category(models.Model):
    # Название категории
    name = models.CharField(max_length=100, verbose_name='наименование')
    # Описание категории
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    # Название продукта
    name = models.CharField(max_length=100, verbose_name='наименование')
    # Описание продукта
    description = models.TextField(blank=True, null=True, verbose_name='описание')
    # Изображение продукта
    image_preview = models.ImageField(default='default.png', upload_to='products/')
    # Все изображения продукта
    images = models.ImageField(default='default.png', upload_to='products/')
    # Категория продукта
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    # Цена продукта
    price = models.FloatField(verbose_name='цена за покупку')
    # Дата создания продукта
    date_creation = models.DateTimeField(default=datetime.now, verbose_name='дата создания')
    # Дата последнего изменения продукта
    date_modification = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    # Менеджер моделей для построения запросов
    objects = models.Manager()

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'{self.name} ({self.category})'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_number = models.IntegerField()
    version_name = models.CharField(max_length=100)
    is_current_version = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product} - Версия  {self.version_number}"


class Contacts(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя контакта', default='')
    country = models.CharField(max_length=50, verbose_name='страна')
    inn = models.CharField(max_length=15, verbose_name='ИНН')
    address = models.CharField(max_length=100, verbose_name='адрес')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    # Заголовок поста
    title = models.CharField(max_length=255, primary_key=True)
    # Слаг поста (для формирования url)
    slug = models.SlugField(max_length=200, unique=True)
    # Содержание поста
    content = models.TextField()
    # Заставка поста
    preview = models.ImageField(upload_to='blog_previews/')
    # Дата создания поста
    created_at = models.DateTimeField(auto_now_add=True)
    # Флаг, является ли пост опубликованным
    is_published = models.BooleanField(default=False)
    # Кол-во просмотров поста
    views_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
