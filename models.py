from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from uuid import uuid4
from inspect import getmembers, isfunction
import importlib

class CleanerTest(models.Model):
	test_id = models.UUIDField(primary_key=True, default=uuid4)
	function_module = models.CharField(max_length=255, null=False)
	function_name = models.CharField(max_length=255, null=False)
	graph_id = models.UUIDField(null=True, blank=True)
	enabled = models.BooleanField(default=False)
	created_time = models.DateTimeField(auto_now_add=True)
	"""A datetime representing the time this object was created."""
	updated_time = models.DateTimeField(auto_now=True)
	"""A datetime representing the time this object was last modified."""

	@property
	def test_passed_count(self):
		return 0

	@property
	def test_failed_count(self):
		return 0

	@property
	def run(self):
		try:
			mod = importlib.import_module(self.function_module)
		except:
			return None
		for fn in getmembers(mod, isfunction):
			if fn[0] == self.function_name:
				return fn[1]
		return None

	def __str__(self):
		return '.'.join([self.function_module, self.function_name])

	class Meta:

		db_table = "cleaner_tests"
		managed = True
		verbose_name = 'test'
		verbose_name_plural = 'tests'

class CleanerTestResult(models.Model):
	run_as_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_results')
	function_run = models.ForeignKey(CleanerTest, on_delete=models.CASCADE, related_name='results')
	subject_resource = models.UUIDField(null=False)
	test_result = models.BooleanField(default=False)
	created_time = models.DateTimeField(auto_now_add=True)
	"""A datetime representing the time this object was created."""
	updated_time = models.DateTimeField(auto_now=True)
	"""A datetime representing the time this object was last modified."""

	def __str__(self):
		if self.test_result:
			return 'Successful run of ' + str(self.function_run) + ' on ' + str(self.subject_resource)
		return 'Unsuccessful run of ' + str(self.function_run) + ' on ' + str(self.subject_resource)

	class Meta:

		db_table = "cleaner_test_results"
		managed = True
		verbose_name = 'test result'
		verbose_name_plural = 'test results'

class CleanerTestEvent(models.Model):
	run_as_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='test_events')
	function_run = models.ForeignKey(CleanerTest, on_delete=models.CASCADE, related_name='events')
	test_passed_count = models.IntegerField()
	test_failed_count = models.IntegerField()
	created_time = models.DateTimeField(auto_now_add=True)
	"""A datetime representing the time this object was created."""
	updated_time = models.DateTimeField(auto_now=True)
	"""A datetime representing the time this object was last modified."""

	def __str__(self):
		return 'Run of ' + str(self.function_run)

	class Meta:

		db_table = "cleaner_test_events"
		managed = True
		verbose_name = 'test run event'
		verbose_name_plural = 'test run events'
