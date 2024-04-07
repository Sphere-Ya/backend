"""Models for Events."""

from django.db import models


































































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
        return f'{self.name}'
