from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class CleanerTest(models.Model):
	test_id = models.UUIDField(primary_key=True)
	function_module = models.CharField(max_length=255, null=False)
	function_name = models.CharField(max_length=255, null=False)
	graph_id = models.UUIDField(null=False)
	enabled = models.BooleanField(default=False)
	created_time = models.DateTimeField(auto_now_add=True)
	"""A datetime representing the time this object was created."""
	updated_time = models.DateTimeField(auto_now=True)
	"""A datetime representing the time this object was last modified."""

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

	class Meta:

		db_table = "cleaner_test_results"
		managed = True
		verbose_name = 'test result'
		verbose_name_plural = 'test results'
