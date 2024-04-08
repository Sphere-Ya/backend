"""Models for Events."""
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.db.models.deletion import CASCADE

User = get_user_model()


class Country(models.Model):
    """Model Country."""
    name = models.CharField(max_length=50,
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
    name = models.CharField(max_length=50,
                            blank=False,
                            verbose_name="Название города",
                            help_text="Введите название города",
                            unique=False,
                            )
    сountry_id = models.ForeignKey(Country,
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
    name = models.CharField(max_length=50,
                        blank=False,
                        verbose_name="Название улицы",
                        help_text="Введите название улицы",
                        unique=False,
                        )
    city_id = models.ForeignKey(City,
                            on_delete=models.CASCADE,
                            blank=False,
                            verbose_name="id города",
                            related_name='streets')

    class Meta:
        ordering = ["name"]
        verbose_name = "Улица"
        verbose_name_plural = "Улицы"

    def __str__(self):
        return f'{self.name}'


class Building(models.Model):
    """Model Building."""
    name = models.CharField(max_length=50,
                            blank=False,
                            verbose_name="Название здания",
                            help_text="Введите название здания",
                            unique=False,
                            )
    latitude = models.FloatField(verbose_name="Широта",
                                 help_text="Введите широту здания",
                                 )
    longitude = models.FloatField(verbose_name="Долгота",
                                  help_text="Введите долготу здания",
                                  )
    street_id = models.ForeignKey(Street,
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
   