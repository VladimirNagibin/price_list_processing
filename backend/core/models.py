from django.db import models

from .constants import MAX_NAME_LENGTH


class CodeNameGroupSubgroupModel(models.Model):
    code = models.SmallIntegerField(
        verbose_name='Код товара от поставщика в 1С'
    )
    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Наименование',
        null=True,
        blank=True,
    )
    brand = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Бренд',
    )
    subgroup = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Подгруппа',
    )
    supplier = models.SmallIntegerField(verbose_name='Код поставщика в 1С')

    class Meta:
        abstract = True
        ordering = ('name', )

    def __str__(self):
        return self.name


class ProductsummarySizeColorModel(models.Model):
    product_summary = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Наименование',
        null=True,
        blank=True,
    )
    size = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Наименование',
        null=True,
        blank=True,
    )
    color = models.CharField(
        max_length=MAX_NAME_LENGTH,
        verbose_name='Наименование',
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True
