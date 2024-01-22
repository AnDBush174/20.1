from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.apps import apps


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    # Получаем модель группы
    Group = apps.get_model('auth', 'Group')

    # Создаем группу модераторов
    moderator_group, created = Group.objects.get_or_create(name='модератор')

    # Получаем разрешения для модели Product
    product_permissions = Permission.objects.filter(content_type__app_label='main', codename__in=['change_product', 'delete_product'])

    # Назначаем разрешения группе модераторов
    moderator_group.permissions.add(*product_permissions)
