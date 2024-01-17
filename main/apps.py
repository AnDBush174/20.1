# main/apps.py
from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)


@receiver(post_migrate)
def create_groups(sender, **kwargs):
    # Создаем группу модераторов
    moderator_group, created = Group.objects.get_or_create(name='модератор')

    # Получаем разрешения для модели Product
    product_permissions = Permission.objects.filter(content_type__app_label='main', codename__in=['change_product', 'delete_product'])

    # Назначаем разрешения группе модераторов
    moderator_group.permissions.add(*product_permissions)
