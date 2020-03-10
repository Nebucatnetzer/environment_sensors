from django.core.management.base import BaseCommand, CommandError
from collector.collector import values_to_db

class Command(BaseCommand):
    help = 'Writes the sense hat values to the db.'

    def handle(self, *args, **options):
        values_to_db()
