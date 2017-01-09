from django.core.management.base import BaseCommand, CommandError
import _scrapedb as scrapedb
import _maketeams as maketeams

class Command(BaseCommand):
    help = 'Scrape footballdb.com to populate database.'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        #maketeams.delete_all_teams()
        #maketeams.make_teams()
        scrapedb.delete_all_players()
        scrapedb.delete_all_colleges()
        scrapedb.run_the_site()