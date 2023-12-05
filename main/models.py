# models.py
from django.db import models
from datetime import datetime
from django.utils.text import slugify


# Модель Категории
class Category(models.Model):
    # Название категории
    name = models.CharField(max_length=100, verbose_name='наименование')
    # Описание категории
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    # Возвращается строковое представление модели
    def __str__(self):
        return self.name


# Модель Продукта
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

    # Возвращается строковое представление модели
    def __str__(self):
        return f'{self.name} ({self.category})'


# Модель Контактов
class Contacts(models.Model):
    # Страна контакта
    country = models.CharField(max_length=50, verbose_name='страна')
    # ИНН контакта
    inn = models.CharField(max_length=15, verbose_name='ИНН')
    # Адрес контакта
    address = models.CharField(max_length=100, verbose_name='адрес')

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'

    # Возвращается строковое представление модели
    def __str__(self):
        return self.inn


# Модель Поста блога
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

    # При сохранении поста, генерируем слаг если пост новый
    def save(self, *args, **kwargs):
        if not self.title:  # Если создается новый объект, то слаг еще не сгенерирован
            self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

    # Возвращается строковое представление модели
    def __str__(self):
        return self.title

