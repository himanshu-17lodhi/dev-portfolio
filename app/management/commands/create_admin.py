from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a superuser if it does not exist'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        username = "himanshu_lodhi"
        email = "lodhihimanshu17@gmail.com"
        password = "Jairajputana@17" 
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
