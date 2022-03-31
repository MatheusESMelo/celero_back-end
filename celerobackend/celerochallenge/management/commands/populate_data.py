from django.core.management.base import BaseCommand
import csv
from celerochallenge.models import AthletesAndResults

class Command(BaseCommand):
    help = 'Popultes database with Kaggle data in csv'

    def handle(self, *args, **options):
        self.create_athletes_and_results()

    def create_athletes_and_results(self):
        with open('athlete_events.csv') as csv_file:
            data = csv.DictReader(csv_file)
            
            athletes_results_batch = []
            for row in data:
                athletes_results = AthletesAndResults(
                    name=row['Name'],
                    sex=row['Sex'],
                    age=row['Age'],
                    height=row['Height'],
                    weight=row['Weight'],
                    team=row['Team'],
                    noc=row['NOC'],
                    games=row['Games'],
                    year=row['Year'],
                    season=row['Season'],
                    city=row['City'],
                    sport=row['Sport'],
                    event=row['Event'],
                    medal=row['Medal'],
                )

                athletes_results_batch.append(athletes_results)

            AthletesAndResults.objects.bulk_create(athletes_results_batch)




        # usar batch_create do django

