from django.db import migrations
from django.contrib.auth.management import create_permissions
from django.apps import apps
from os import error
from django.contrib.auth.hashers import make_password

def create_applications_permissions():
    try:
        for app_config in apps.get_app_configs():
            create_permissions(app_config)
    except(LookupError, ImportError) as e:
        raise error("%s. Are you sure your INSTALLED_APPS setting is correct?" % e)


def insert_data(apps, schema_migration):
    create_applications_permissions()
    User = apps.get_model('auth', 'User')

    user1 = User(id=1,username="user1",email='user1@example.com')
    user1.password = make_password("Prueba_123")
    user1.save()

    user2 = User(id=2,username="user2",email='user2@example.com')
    user2.password = make_password("Prueba_123")
    user2.save()

    user3 = User(id=3,username="user3",email='user3@example.com')
    user3.password = make_password("Prueba_123")
    user3.save()


class Migration(migrations.Migration):
        
    dependencies = [
        ('api','0001_initial'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]