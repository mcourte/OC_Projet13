# lettings/migrations/0002_migrate_data.py
from django.db import migrations


def migrate_address_data(apps, schema_editor):
    try:
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
    except LookupError:
        return
    NewAddress = apps.get_model('lettings', 'Address')
    for address in OldAddress.objects.all():
        NewAddress.objects.create(
            id=address.id,
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code
        )


def migrate_letting_data(apps, schema_editor):
    try:
        OldLetting = apps.get_model('oc_lettings_site', 'Letting')
        OldAddress = apps.get_model('oc_lettings_site', 'Address')
    except LookupError:
        return
    NewLetting = apps.get_model('lettings', 'Letting')
    NewAddress = apps.get_model('lettings', 'Address')
    address_map = {old_address.id: NewAddress.objects.get(street=old_address.street, number=old_address.number) for old_address in OldAddress.objects.all()}
    for old_letting in OldLetting.objects.all():
        new_address = address_map[old_letting.address_id]
        NewLetting.objects.create(
            title=old_letting.title,
            address=new_address
        )

class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),

    ]

    operations = [
        migrations.RunPython(migrate_address_data),
        migrations.RunPython(migrate_letting_data),
    ]
