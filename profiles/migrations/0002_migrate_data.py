# profiles/migrations/0002_migrate_data.py
from django.db import migrations


def migrate_profile_data(apps, schema_editor):
    try:
        OldProfile = apps.get_model('oc_lettings_site', 'Profile')
    except LookupError:
        return
    NewProfile = apps.get_model('profiles', 'Profile')
    user = apps.get_model('auth', 'User')

    user_map = {user.id: user for user in user.objects.all()}

    for OldProfile in OldProfile.objects.all():
        user = user_map[OldProfile.user_id]
        NewProfile.objects.create(
            user=user,
            favorite_city=OldProfile.favorite_city
        )

class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),

    ]

    operations = [
        migrations.RunPython(migrate_profile_data),
    ]
