from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from django.contrib.auth.models import User
from cleaner.models import CleanerTest
from cleaner.util.exec import run_test
from cleaner.util.display import test_functions
import sys, pyprind

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

	def run_test(self, test, user):

		ret = run_test(test, user, "█")

	def handle(self, *args, **kwargs):

		if not 'test' in kwargs:
			sys.exit(1)

		try:
			test = CleanerTest.objects.get(test_id=kwargs['test'])
		except:
			test = None
		if test is None:
			try:
				test = CleanerTest.objects.get(function_name=kwargs['test'])
			except:
				test = None
		if test is None:
			full_path = str(kwargs['test']).split('.')
			try:
				test = CleanerTest.objects.get(function_module='.'.join(full_path[0:-1]), function_name=full_path[-1])
			except:
				test = None

		try:
			user = User.objects.filter(is_superuser=True).first()
		except:
			user = None
		if user is None:
			try:
				user = User.objects.filter(is_staff=True).first()
			except:
				user = None
		if user is None:
			try:
				user = User.objects.first()
			except:
				user = None

		if test is None:
			for test_obj in test_functions():
				try:
					test = CleanerTest.objects.get(test_id=test_obj['test_id'])
				except:
					test = None
				if test is None:
					continue
				self.run_test(test, user)
		else:
			self.run_test(test, user)

