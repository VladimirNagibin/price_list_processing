import pandas as pd
import sqlite3

from django.core.management.base import BaseCommand
# from django.db.models import Max


class Command(BaseCommand):
    def load_data(self, file, table):
        connection = sqlite3.connect('db.sqlite3')
        contents = pd.read_csv(
            file,
            # encoding='ANSI',
            sep=';',
            escapechar='\\')
        contents.to_sql(
            table,
            connection,
            if_exists='replace',  # append replace
            index=False,
            chunksize=10000,
        )

    def handle(self, *args, **kwargs):
        ...
        self.load_data(
            'data/Tab_out1.txt',
            'products_codesupplierbase',
        )
        #self.load_data(
        #    'data/Tab_out.txt',
        #    'products_codesupplierfile',
        #)

    def add_arguments(self, parser):
        parser.add_argument(
            '-e',
            '--erase',
            action='store_true',
            default=False,
            help='Очистить таблицу перед загрузкой'
        )
