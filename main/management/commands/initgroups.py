# config/main/management/commands/initgroups.py
from django.contrib.auth.models import Group, Permission
from django.apps import apps
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Initialize groups and permissions'

    def handle(self, *args, **options):
        # Tip: replace 'main.Product' with the correct app_label.model_name of your Product model
        product_model = apps.get_model('main', 'Product')
        product_permissions = Permission.objects.filter(content_type__app_label=product_model._meta.app_label, codename__in=['change_product', 'delete_product'])

        moderator_group, created = Group.objects.get_or_create(name='модератор')
        moderator_group.permissions.add(*product_permissions)

        self.stdout.write(self.style.SUCCESS('Successfully initialized groups and permissions'))
