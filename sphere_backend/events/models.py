"""Models for Events."""

from django.db import models




















class City(models.Model):
    """Model City."""
    name = models.CharField(max_length=50,
                            blank=False,
                            verbose_name="Название города",
                            help_text="Введите название города",
                            unique=False,  # False or True. Что то переклинило
                            )
    country_id = models.ForeignKey(Country,
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
