# Generated by Django 4.2.9 on 2024-04-05 13:27

from django.db import migrations


def add_data(apps, schema_editor):
    EventSpecialization = apps.get_model("events", "EventSpecialization")
    data = [
        {
            'id': 1,
            'name': 'Анализ данных',
        },
        {
            'id': 2,
            'name': 'Маркетинг'
        },
        {
            'id': 3,
            'name': 'Разработка'
        },
        {
            'id': 4,
            'name': 'Python'
        },
        {
            'id': 5,
            'name': 'TypeScript'
        },
        {
            'id': 6,
            'name': 'Angular'
        },
        {
            'id': 7,
            'name': 'React'
        },
        {
            'id': 8,
            'name': 'Javascript'
        },
        {
            'id': 9,
            'name': 'Java'
        },
        {
            'id': 10,
            'name': 'C++'
        },
        {
            'id': 11,
            'name': 'Другое'
        },
        {
            'id': 12,
            'name': 'Kotlin'
        },
        {
            'id': 13,
            'name': 'Swift'
        }
    ]
    for row in data:
        EventSpecialization.objects.update_or_create(**row)

    Interest = apps.get_model("events", "Interest")
    print(EventSpecialization.objects.filter(id=3))
    odj, _ = Interest.objects.get_or_create(
        id=1,
        name='Backend',
    )
    odj.event_specializations.add(3)
    odj.event_specializations.add(4)
    odj.event_specializations.add(9)
    odj.event_specializations.add(10)
    odj.event_specializations.add(11)
    odj, _ = Interest.objects.get_or_create(
        id=2,
        name='Frontend',
    )
    odj.event_specializations.add(3)
    odj.event_specializations.add(5)
    odj.event_specializations.add(6)
    odj.event_specializations.add(7)
    odj.event_specializations.add(8)
    odj.event_specializations.add(11)
    odj, _ = Interest.objects.get_or_create(
        id=3,
        name='Mobile',
    )
    odj.event_specializations.add(3)
    odj.event_specializations.add(12)
    odj.event_specializations.add(13)
    odj.event_specializations.add(11)
    odj, _ = Interest.objects.get_or_create(
        id=4,
        name='QA',
    )
    odj.event_specializations.add(4)
    odj, _ = Interest.objects.get_or_create(
        id=5,
        name='ML',
    )
    odj.event_specializations.add(1)
    odj, _ = Interest.objects.get_or_create(
        id=6,
        name='Другое',
    )
    odj.event_specializations.add(2)


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_data),
    ]