"""Models for Events."""

from django.db import models











































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
