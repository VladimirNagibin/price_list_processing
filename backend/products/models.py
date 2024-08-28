from django.db import models

from core.constants import MAX_NAME_LENGTH
from core.models import CodeNameGroupSubgroupModel


class CodeSupplierBase(CodeNameGroupSubgroupModel):

    class Meta:
        verbose_name = 'код поставщика 1с'
        verbose_name_plural = 'Коды поставщиков 1с'


class CodeSupplierFile(CodeNameGroupSubgroupModel):
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
        verbose_name = 'код поставщика в файле'
        verbose_name_plural = 'Коды поставщиков в файле'
