from cleaner.models import CleanerTest

def run_test(cleaner_test, resource):

	if cleaner_test.run is None:
		return False
	return cleaner_test.run(resource)
