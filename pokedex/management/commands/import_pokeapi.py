from django.core.management import BaseCommand, CommandError
from ._import_functions import import_pokemon


class Command(BaseCommand):
    help = "Import the all Generation 1 Pokemon and their complete evolution trees into the database."

    def add_arguments(self, parser):
        parser.add_argument(
            "--verbose",
            action="store_true",
            help="Enable verbose output.",
        )

    def handle(self, *args, **options):
        verbose = options.get("verbose", False)

        for i in range(1, 152):
            import_pokemon(i, verbose=verbose, stdout=self.stdout)

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully imported all Generation 1 Pokemon and their complete evolution trees."
            )
        )
