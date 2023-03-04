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
    Transaction = apps.get_model('api', 'Transaction')

    t1 = Transaction.objects.create(id = 1, name = "Cambio de contraseña")
    t2 = Transaction.objects.create(id = 2, name = "Acceso a la banca web")
    t3 = Transaction.objects.create(id = 3, name = "Acceso desde la banca móvil" )


class Migration(migrations.Migration):
        
    dependencies = [
        ('api','0003_transaction_alter_token_user_token_transaction'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]