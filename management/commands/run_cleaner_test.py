from django.core.management.base import BaseCommand, CommandError
from cleaner.models import CleanerTest

class Command(BaseCommand):
	"""
	Command for running Arches Cleaner tests.
	"""
	def add_arguments(self, parser):

		parser.add_argument(
			"-t",
			"--test",
			action="store",
			dest="test",
			default=None,
			help="The ID (either UUID or function name) of a test you would like to run.",
		)

	def handle(self, *args, **kwargs):
		print(kwargs)

