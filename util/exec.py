from cleaner.models import CleanerTest, CleanerTestEvent, CleanerTestResult

def run_test(cleaner_test, resource, user):

	if cleaner_test.run is None:
		res = False
	else:
		res = cleaner_test.run(resource)

	ret = CleanerTestResult(run_as_user=user, function_run=cleaner_test, subject_resource=resource.pk, test_result=res)
	ret.save()
	return ret
