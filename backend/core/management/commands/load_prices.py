from django.core.management.base import BaseCommand

from products.servises import parse_files


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        parse_files()

    def add_arguments(self, parser):
        parser.add_argument(
            '-e',
            '--erase',
            action='store_true',
            default=False,
            help='Очистить таблицу перед загрузкой'
        )
