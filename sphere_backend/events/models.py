"""Models for Events."""

from django.db import models


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
