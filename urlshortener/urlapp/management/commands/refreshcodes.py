from django.core.management.base import BaseCommand, CommandError
from urlapp.models import URLAppShortener


class Command(BaseCommand):
    help = 'Refreshes all URLAppShortener shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return URLAppShortener.objects.refresh_shortener(items=options['items'])
