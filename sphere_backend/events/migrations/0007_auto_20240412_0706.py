# Generated by Django 4.2.9 on 2024-04-12 04:06

from django.db import migrations


def add_data(apps, schema_editor):
    Country = apps.get_model("events", "Country")
    Country.objects.get_or_create(
        id=1,
        name='Russia'
    )

    City = apps.get_model("events", "City")
    City.objects.get_or_create(
        id=1,
        name='Москва',
        country_id=1,
    )

    City = apps.get_model("events", "City")
    City.objects.get_or_create(
        id=2,
        name='Санкт-Петербург',
        country_id=1,
    )

    City = apps.get_model("events", "City")
    City.objects.get_or_create(
        id=3,
        name='Сочи',
        country_id=1,
    )

    Street = apps.get_model("events", "Street")
    Street.objects.get_or_create(
        id=1,
        name='Арбат',
        city_id=1,
    )

    Street = apps.get_model("events", "Street")
    Street.objects.get_or_create(
        id=2,
        name='Тверская',
        city_id=1,
    )

    Street = apps.get_model("events", "Street")
    Street.objects.get_or_create(
        id=3,
        name='Малая Содовая',
        city_id=2,
    )

    Street = apps.get_model("events", "Street")
    Street.objects.get_or_create(
        id=4,
        name='Большая Морская',
        city_id=2,
    )

    Street = apps.get_model("events", "Street")
    Street.objects.get_or_create(
        id=5,
        name='Навагинска',
        city_id=3,
    )

    Street = apps.get_model("events", "Street")
    Street.objects.get_or_create(
        id=6,
        name='Нагорная',
        city_id=3,
    )

    Building = apps.get_model("events", "Building")
    Building.objects.get_or_create(
        id=1,
        name='32',
        street_id=1,
        latitude=55.749096,
        longitude=37.589599,
    )

    Building = apps.get_model("events", "Building")
    Building.objects.get_or_create(
        id=2,
        name='3',
        street_id=2,
        latitude=55.757369,
        longitude=37.612991,
    )

    Building = apps.get_model("events", "Building")
    Building.objects.get_or_create(
        id=3,
        name='8',
        street_id=3,
        latitude=59.934619,
        longitude=30.337787,
    )

    Building = apps.get_model("events", "Building")
    Building.objects.get_or_create(
        id=4,
        name='55',
        street_id=4,
        latitude=59.931287,
        longitude=30.302339,
    )

    Building = apps.get_model("events", "Building")
    Building.objects.get_or_create(
        id=5,
        name='9Д',
        street_id=5,
        latitude=43.587912,
        longitude=39.723631,
    )

    Building = apps.get_model("events", "Building")
    Building.objects.get_or_create(
        id=6,
        name='14',
        street_id=6,
        latitude=43.578198,
        longitude=39.730078,
    )


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_participant_speaker_speaker_speaker_user_event_and_more'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]
