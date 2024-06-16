from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from catalog.models import Product


class Command(BaseCommand):
    help = 'Create moderator group and assign permissions'

    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(name='Moderators') # Create group

        product_content_type = ContentType.objects.get_for_model(Product)  # No idea what this does

        permissions = [
            'can_unpublish_product',
            'can_edit_product',
            'can_change_product_category',
        ]  # definig the permissions

        for perm in permissions:  # Giving permissions to the group
            permission = Permission.objects.get(codename=perm, content_type=product_content_type)
            moderator_group.permissions.add(permission)
