from django.core.management.base import BaseCommand, CommandError
import _writeout as writeout

class Command(BaseCommand):
    help = 'write the content of this database to csv files.'

    def add_arguments(self, parser):
        #parser.add_argument('poll_id', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        writeout.write_players()
        writeout.write_teams()
        writeout.write_colleges()
        writeout.write_highschools()