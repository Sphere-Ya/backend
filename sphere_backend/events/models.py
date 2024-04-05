from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

User = get_user_model()


class EventSpecialization(models.Model):
    """Справочник специализаций."""
    name = models.CharField('Название специализации', max_length=250)

    class Meta:
        verbose_name = 'Специализация'
        verbose_name_plural = 'Специализации'

    def __str__(self):
        return self.name


class Interest(models.Model):
    """Справочник направлений работы."""
    name = models.CharField('Название направления', max_length=250)
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
    name = models.CharField('Название файла', max_length=250)
    link = models.URLField('Ссылка на файл', blank=False)

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

    def __str__(self):
        return self.name

class Event(models.Model):
  # event =
      name = models.CharField('Название события', max_length=250)
      description = models.TextField('Описание')
      started_at = models.DateTimeField(verbose_name='Дата начала события')
      ended_at = models.DateTimeField(verbose_name='Дата окончания события')
      link = models.URLField('Ссылка на трансляцию', blank=True, null=True)
      building_id = models.PositiveIntegerField ('Адрес') # Заглушка, связь со справочником
      address_comment = models.TextField('Как добраться', max_length=250)
      event_specializations = models.ManyToManyField(
            EventSpecialization,
            related_name='events',
            blank=True,
            verbose_name='Специализации',
        )
      speakers = models.ManyToManyField(
            EventSpecialization,
            related_name='events',
            blank=True,
            verbose_name='Специализации',
        )
