import requests

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from base.models import Game


class Command(BaseCommand):
    help = "Imports games from Giant Bomb API"
    headers = {'user-agent': 'arcademachine/0.0.1'}
    platforms = 84  # Arcade platform

    def get_total_results(self, api_key):
        payload = {
            'api_key': api_key,
            'format': "json",
            'limit': 1,
            'offset': 0,
            'field_list': 'id',
            'platforms': self.platforms,
        }

        response = requests.get(
            "https://www.giantbomb.com/api/games/", headers=self.headers, params=payload)

        total_results = 0
        if response.status_code == 200:
            total_results = response.json()['number_of_total_results']
        else:
            raise CommandError(f"Received status code {response.status_code} from GB API")
        return total_results

    def pull_page(self, page_number, page_size, api_key):
        offset = page_number * page_size
        print("Pulling games from {} to {}".format(offset, offset + page_size))
        payload = {
            'api_key': api_key,
            'format': "json",
            'limit': page_size,
            'offset': offset,
            'field_list': 'id,guid,name,aliases,original_release_date',
            'platforms': self.platforms,
        }
        headers = {'user-agent': 'arcademachine/0.0.1'}
        response = requests.get(
            "https://www.giantbomb.com/api/games/", headers=headers, params=payload)

        games = {'results': []}
        if response.status_code == 200:
            games = response.json()
        else:
            raise CommandError(f"Received status code {response.status_code} from GB API")
        return games.get('results')

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Reset games list before import",
        )

    def handle(self, *args, **options):
        # total_results = 3167
        total_results = self.get_total_results(settings.GIANTBOMB_API_KEY)
        page_size = 100
        pages = int((total_results / page_size) + 1)

        print(f"Pulling info for {total_results} arcade games.")
        games = []
        for page in range(0, pages):
            games += self.pull_page(page, page_size, settings.GIANTBOMB_API_KEY)

        print('Found {} games.'.format(len(games)))

        if options['reset']:
            Game.objects.all().delete()
        for game in games:
            aliases = game.get('aliases') if game.get('aliases') is not None else ''
            Game.objects.create(
                giantbomb_id=game.get('id'),
                giantbomb_guid=game.get('guid'),
                release_date=game.get('original_release_date'),
                name=game.get('name'),
                aliases=aliases
            )
        print("Done.")
