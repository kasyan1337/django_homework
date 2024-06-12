from users.models import CustomUser
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        user = CustomUser.objects.create(email='admin@email.com')
        user.set_password("123456")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

