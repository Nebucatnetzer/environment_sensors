from django.core.management.base import BaseCommand, CommandError
from collector.collector import clean_db

class Command(BaseCommand):
    help = 'Clean out values older than 30 days.'

    def handle(self, *args, **options):
        clean_db()
