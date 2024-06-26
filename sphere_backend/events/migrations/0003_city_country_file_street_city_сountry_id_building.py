# Generated by Django 4.2.9 on 2024-04-08 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_added_interest_eventspecialization_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    help_text='Введите название города',
                    max_length=50,
                    verbose_name='Название города'
                )),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    help_text='Введите название страны',
                    max_length=50,
                    unique=True,
                    verbose_name='Название страны'
                )),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    max_length=250,
                    verbose_name='Название файла'
                )),
                ('link', models.URLField(
                    verbose_name='Ссылка на файл'
                )),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False, verbose_name='ID'
                )),
                ('name', models.CharField(
                    help_text='Введите название улицы',
                    max_length=50,
                    verbose_name='Название улицы'
                )),
                ('city_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='streets',
                    to='events.city',
                    verbose_name='id города'
                )),
            ],
            options={
                'verbose_name': 'Улица',
                'verbose_name_plural': 'Улицы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='сountry_id',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='cities',
                to='events.country',
                verbose_name='id страны'
            ),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID'
                )),
                ('name', models.CharField(
                    help_text='Введите название здания',
                    max_length=50,
                    verbose_name='Название здания'
                )),
                ('latitude', models.FloatField(
                    help_text='Введите широту здания',
                    verbose_name='Широта'
                )),
                ('longitude', models.FloatField(
                    help_text='Введите долготу здания',
                    verbose_name='Долгота'
                )),
                ('street_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='buildings',
                    to='events.street',
                    verbose_name='id улицы'
                )),
            ],
            options={
                'verbose_name': 'Здание',
                'verbose_name_plural': 'Здания',
                'ordering': ['name'],
            },
        ),
    ]
