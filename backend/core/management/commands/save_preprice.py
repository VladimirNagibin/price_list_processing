import pandas as pd
import sqlite3

from django.core.management.base import BaseCommand

# from products.models import PriceSupplier


class Command(BaseCommand):

    def save_price_as_is(self):
        connection = sqlite3.connect('db.sqlite3')
        data_frame = pd.read_sql('SELECT * FROM products_pricesupplier',
                                 connection)
        excel_file_path = 'data/exported_data.xlsx'
        data_frame.to_excel(excel_file_path, index=False)

    def save_price_for_load(self):
        connection = sqlite3.connect('db.sqlite3')
        data_frame = pd.read_sql(
            'SELECT * FROM products_pricesupplier ORDER BY brand, subgroup, name',
            connection
        )
        excel_file_path = 'data/price.xlsx'
        # data_frame.to_excel(excel_file_path, index=False)
        brand = ''
        subgroup = ''
        price_all = []
        price_all.append(['', '', ''])
        for s in data_frame.itertuples():
            brand_current = s.brand
            subgroup_current = s.subgroup
            code = s.code
            name = s.name
            price = s.price
            if brand != brand_current:
                brand = brand_current
                # print(f'{brand} =================')
                price_all.append(['', brand, ''])
            if subgroup != subgroup_current:
                subgroup = subgroup_current
                price_all.append(['', subgroup, ''])
                # print(f'{subgroup} ---------------')
            # print(code, name, price)
            price_all.append([code, name, price])
        df = pd.DataFrame(price_all, columns=['code', 'name', 'price'])
        df.to_excel(excel_file_path, index=False)

    def handle(self, *args, **kwargs):
        if kwargs['for_code']:
            self.save_price_as_is()
        elif kwargs['for_price']:
            self.save_price_for_load()

    def add_arguments(self, parser):
        parser.add_argument(
            '-c',
            '--for_code',
            action='store_true',
            default=False,
            help='Сохранить общую таблицу для догрузки кодов'
        )
        parser.add_argument(
            '-p',
            '--for_price',
            action='store_true',
            default=False,
            help='Сохранить прайс для загрузки'
        )
