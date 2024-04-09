# Generated by Django 4.2.9 on 2024-04-09 18:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_city_country_file_street_city_сountry_id_building'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=200, verbose_name='Эл. почта')),
                ('phone', models.CharField(max_length=11, verbose_name='Телефон')),
                ('job_position', models.CharField(max_length=300, verbose_name='Место работы')),
                ('job_title', models.CharField(max_length=200, verbose_name='Должность')),
                ('experience', models.CharField(choices=[('Нет опыта', 'Нет опыта'), ('От 1 года', 'От 1 года'), ('От 3 лет', 'От 3 лет'), ('От 5 лет', 'От 5 лет'), ('Другое', 'Другое')], default='Нет опыта', max_length=50, verbose_name='Опыт работы')),
                ('event_specializations', models.ManyToManyField(to='events.eventspecialization', verbose_name='Специализация')),
                ('interests', models.ManyToManyField(to='events.interest', verbose_name='Интересы')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_anketa', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Анкета пользователя',
            },
        ),
    ]
