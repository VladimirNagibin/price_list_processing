import numpy as np
import pandas as pd

from django.core.management.base import BaseCommand

from products.models import CodeSupplierFile, PriceSupplier


class Command(BaseCommand):
    def load_data(self, file, table):
        # connection = sqlite3.connect('db.sqlite3')
        contents = pd.read_csv(
            file,
            # encoding='ANSI',
            sep=';',
            escapechar='\\')
        contents.to_sql(
            table,
        #    connection,
            if_exists='replace',  # append replace
            index=False,
            chunksize=10000,
        )

    def update_codes(self):
        update_queries = []
        add_queries = []
        # print(datetime.datetime.now().time())
        # print(f'----------- {file} ---------------')
        file = 'data/exported_data.xlsx'
        inf = pd.read_excel(file)
        for s in inf.itertuples():
            product_price = PriceSupplier.objects.get(id=s.id)
            product_price.brand = s.brand
            product_price.subgroup = s.subgroup
            update_queries.append(product_price)
            # print(s.id)
            product_added = CodeSupplierFile(
                code=s.code,
                name=s.name,
                brand=s.brand,
                subgroup=s.subgroup,
                supplier=s.supplier,
                product_summary=s.product_summary,
                size=s.size,
                color=s.color,
            )
            add_queries.append(product_added)
        PriceSupplier.objects.bulk_update(update_queries,
                                          ['brand', 'subgroup'])
        CodeSupplierFile.objects.bulk_create(add_queries)

    def handle(self, *args, **kwargs):
        self.update_codes()

    def add_arguments(self, parser):
        parser.add_argument(
            '-e',
            '--erase',
            action='store_true',
            default=False,
            help='Очистить таблицу перед загрузкой'
        )
