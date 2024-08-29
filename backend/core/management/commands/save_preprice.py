import pandas as pd
import sqlite3

from django.core.management.base import BaseCommand

# from products.models import PriceSupplier


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        # PriceSupplier.objects.all().delete()
        connection = sqlite3.connect('db.sqlite3')
        data_frame = pd.read_sql('SELECT * FROM products_pricesupplier',
                                 connection)
        excel_file_path = 'data/exported_data.xlsx'
        data_frame.to_excel(excel_file_path, index=False)

    def add_arguments(self, parser):
        parser.add_argument(
            '-e',
            '--erase',
            action='store_true',
            default=False,
            help='Очистить таблицу перед загрузкой'
        )
