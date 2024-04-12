"""Models for Events."""
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.deletion import CASCADE

User = get_user_model()


class Country(models.Model):
    """Model Country."""
    name = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Название страны",
        help_text="Введите название страны",
        unique=True,
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    """Model City."""
    name = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Название города",
        help_text="Введите название города",
        unique=False,
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="id страны",
        related_name='cities')

    class Meta:
        ordering = ["name"]
        verbose_name = "Город"
        verbose_name_plural = "Города"

    def __str__(self):
        return f'{self.name}'


class Street(models.Model):
    """Model Street."""
    name = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Название улицы",
        help_text="Введите название улицы",
        unique=False,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="id города",
        related_name='streets'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"

    def __str__(self):
        return f'{self.name}'


class Building(models.Model):
    """Model Building."""
    name = models.CharField(
        max_length=50,
        blank=False,
        verbose_name="Название здания",
        help_text="Введите название здания",
        unique=False,
    )
    latitude = models.FloatField(
        verbose_name="Широта",
        help_text="Введите широту здания",
    )
    longitude = models.FloatField(
        verbose_name="Долгота",
        help_text="Введите долготу здания",
    )
    street = models.ForeignKey(
        Street,
        on_delete=models.CASCADE,
        blank=False,
        verbose_name="id улицы",
        related_name='buildings'
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Здание"
        verbose_name_plural = "Здания"

    def __str__(self):
        return self.name


class EventSpecialization(models.Model):
    """Справочник специализаций."""
    name = models.CharField(
        verbose_name='Название специализации',
        max_length=250
    )

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Interest(models.Model):
    """Справочник направлений работы."""
    name = models.CharField(
        verbose_name='Название направления',
        max_length=250
    )
    event_specializations = models.ManyToManyField(
        EventSpecialization,
        related_name='interests',
        blank=True,
        verbose_name='Специализации',
    )

    class Meta:
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'

    def __str__(self):
        return self.name


class File(models.Model):
    """"Модель для файлов"""
    name = models.CharField(
        verbose_name='Название файла',
        max_length=250,
        blank=False
    )
    link = models.URLField(
        verbose_name='Ссылка на файл',
        blank=False
    )

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name


class Anketa(models.Model):
    """Анкета пользователя."""
    NONE = 'Нет опыта'
    BEGINNER = 'От 1 года'
    EXPERIENCE_3 = 'От 3 лет'
    EXPERIENCE_5 = 'От 5 лет'
    OTHER = 'Другое'
    EXPERIENCE_NAME = (
        (NONE, NONE),
        (BEGINNER, BEGINNER),
        (EXPERIENCE_3, EXPERIENCE_3),
        (EXPERIENCE_5, EXPERIENCE_5),
        (OTHER, OTHER),
    )
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='user_anketa'
    )
    first_name = models.CharField(
        max_length=200,
        verbose_name='Имя',
        db_index=True
    )
    last_name = models.CharField(
        max_length=200,
        verbose_name='Фамилия'
    )
    email = models.EmailField(
        max_length=200,
        verbose_name='Эл. почта'
    )
    phone = models.CharField(
        max_length=11,
        verbose_name='Телефон'
    )
    job_position = models.CharField(
        max_length=300,
        verbose_name='Место работы'
    )
    job_title = models.CharField(
        max_length=200,
        verbose_name='Должность'
    )
    experience = models.CharField(
        max_length=50,
        choices=EXPERIENCE_NAME,
        default=NONE,
        verbose_name='Опыт работы'
    )
    event_specializations = models.ManyToManyField(
        EventSpecialization,
        verbose_name='Специализация',
        related_name='anketa',

    )
    interests = models.ManyToManyField(
        Interest,
        verbose_name='Интересы',
        related_name='anketa',
    )

    class Meta:
        verbose_name_plural = 'Анкета пользователя'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Event(MPTTModel):
    """Справочник события (конференции). Имеет структуру дерева"""
    name = models.CharField(
        verbose_name='Название события',
        max_length=250,
        blank=False,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )
    description = models.TextField(
        verbose_name='Описание события',
        blank=True,
    )
    started_at = models.DateTimeField(
        verbose_name='Дата начала события',
        blank=True,  # Цикличные события без дат
    )
    ended_at = models.DateTimeField(
        verbose_name='Дата окончания события',
        blank=True,
    )
    is_online = models.BooleanField(
        verbose_name='Онлайн',
        default=False
    )
    link = models.URLField(
        verbose_name='Ссылка на трансляцию',
        blank=True,
        null=True
    )
    is_offline = models.BooleanField(
        verbose_name='Оффлайн',
        default=False
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='events',
        verbose_name='ID дома (адрес)',

    )
    address_comment = models.TextField(
        verbose_name='Как добраться',
        max_length=250,
        blank=True,
    )
    event_specializations = models.ManyToManyField(
        EventSpecialization,
        related_name='events',
        blank=True,
        verbose_name='Специализации',
    )
    files = models.ManyToManyField(
        File,
        related_name='events',
        blank=True,
        verbose_name='Файлы',
    )

    class MPTTMeta:
        order_insertion_by = ['started_at']

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'

    def __str__(self):
        return self.name


class Participant(models.Model):
    """Модель участника события"""
    NEW = 'new'
    ACCEPTED = 'accepted'
    CANCELED = 'canceled'
    STATUS_PARTICIPANT = (
        (NEW, 'new'),
        (ACCEPTED, 'accepted'),
        (CANCELED, 'canceled'),
    )
    ON = 'online'
    OFF = 'offline'
    FORMAT = (
        (ON, 'online'),
        (OFF, 'offline'),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='participant',
        verbose_name='ID пользователя',

    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participant',
        help_text='Конференция, на которую подписались',
        verbose_name='ID конференции',

    )
    participation_format = models.CharField(
        max_length=16,
        choices=FORMAT,
        default=ON
    )
    status = models.CharField(
        max_length=16,
        choices=STATUS_PARTICIPANT,
        default=NEW
    )
    # Предлагаю еще добавить дату подписки

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'event'],
                name='participant_user_event'
            )
        ]
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return f'Подписка пользователя {self.user} -> конференцию {self.event}'


class Speaker(models.Model):
    """Модель спикера события"""
    participant = models.ForeignKey(
        Participant,
        on_delete=models.CASCADE,
        related_name='speakers',
        verbose_name='ID участника',

    )
    event = models.ForeignKey(
      Event,
      on_delete=models.CASCADE,
      related_name='speakers',
      help_text='Конференция, на которую подписались',
      verbose_name='ID конференции',

    )
    # Заглушка 'Speeacker, main speacker, co-speacker, poster session speacker and so on'
    # Решить: отдельный справочник или массив
    type = models.CharField(
        max_length=16,
        default='speaker'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['participant', 'event'],
                name='speaker_user_event'
            )
        ]
        verbose_name = 'Спикер'
        verbose_name_plural = 'Спикеры'

    def __str__(self):
        return f'Спикер: участник {self.participant} -> конференцию {self.event}'
