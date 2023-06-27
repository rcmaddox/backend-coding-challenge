import csv
import sys

from django.core.management.base import BaseCommand
from suggestions.models import City
class Command(BaseCommand):
    help = 'Load city data from cities_canada-usa.tsv into the City model'

    def handle(self, *args, **options):
        with open('./suggestions/management/commands/cities_canada-usa.tsv', 'r') as f:
            reader = csv.DictReader(f, delimiter='\t')
            csv.field_size_limit(sys.maxsize)  # Prevents error with large fields
            for row in reader:
                city, created = City.objects.get_or_create(
                    name=row['name'],
                    defaults={

                        'latitude': float(row['lat']),
                        'longitude': float(row['long']),
                        'country': str(row['country']),
                    }
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded city data'))
