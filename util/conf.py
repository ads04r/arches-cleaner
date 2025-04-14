from cleaner.models import CleanerTest, CleanerTestEvent, CleanerTestResult

def enable_test(test_id):

	try:
		test = CleanerTest.objects.get(test_id=test_id)
	except:
		return False
	if test.enabled == False:
		test.enabled = True
		test.save(update_fields=['enabled'])
	return True

def disable_test(test_id):

	try:
		test = CleanerTest.objects.get(test_id=test_id)
	except:
		return False
	if test.enabled == True:
		test.enabled = False
		test.save(update_fields=['enabled'])
	return True

def set_test_graph(test_id, graph_id):

	try:
		test = CleanerTest.objects.get(test_id=test_id)
	except:
		return False
	if test.graph_id != graph_id:
		test.graph_id = graph_id
		test.save(update_fields=['graph_id'])
	return True
