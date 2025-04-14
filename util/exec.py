from cleaner.models import CleanerTest, CleanerTestEvent, CleanerTestResult
from arches.app.models import models
import pyprind, sys

def run_single_test(cleaner_test, resource, user):

	if cleaner_test.run is None:
		res = False
	else:
		res = cleaner_test.run(resource)

	ret = CleanerTestResult(run_as_user=user, function_run=cleaner_test, subject_resource=resource.pk, test_result=res)
	ret.save()
	return ret

def run_test(cleaner_test, user, bar_char=''):

	bar = None
	graph = models.ResourceInstance.objects.filter(graph_id=cleaner_test.graph_id)
	if len(bar_char) > 0:
		bar = pyprind.ProgBar(graph.count(), bar_char="█", stream=sys.stderr, title=str(cleaner_test))

	pass_count = 0
	for res in graph.all():
		test_result = run_single_test(cleaner_test, res, user)
		if test_result.test_result:
			pass_count = pass_count + 1
		if bar:
			bar.update()
	fail_count = graph.count() - pass_count

	ret = CleanerTestEvent(function_run=cleaner_test, run_as_user=user, test_passed_count=pass_count, test_failed_count=fail_count)
	ret.save()

	return ret

