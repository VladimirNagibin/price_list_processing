from django.db import models

from core.constants import MAX_NAME_LENGTH
from core.models import (CodeNameGroupSubgroupModel,
                         ProductsummarySizeColorModel)


class CodeSupplierBase(CodeNameGroupSubgroupModel):

    class Meta:
        verbose_name = 'код поставщика 1с'
        verbose_name_plural = 'Коды поставщиков 1с'


class CodeSupplierFile(CodeNameGroupSubgroupModel,
                       ProductsummarySizeColorModel):

    class Meta:
        verbose_name = 'код поставщика в файле'
        verbose_name_plural = 'Коды поставщиков в файле'


class PriceSupplier(CodeNameGroupSubgroupModel,
                    ProductsummarySizeColorModel):
    price = models.FloatField('Цена')

    class Meta:
        verbose_name = 'прайс поставщика'
        verbose_name_plural = 'Прайсы'
