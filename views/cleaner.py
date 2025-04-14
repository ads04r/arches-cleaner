from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from ..util.display import test_functions, graphs
from ..util.conf import enable_test, disable_test, set_test_graph

import json

@method_decorator(csrf_exempt, name="dispatch")
class CleanerDashboard(View):

	def get(self, request):
		data = {
			'tests': test_functions(),
			'graphs': graphs()
		}
		return JsonResponse(data)

	def post(self, request):
		for test in json.loads(request.body.decode("utf-8")):
			test_id = test['test_id']
			if test['enabled'] == True:
				enable_test(test_id)
			if test['enabled'] == False:
				disable_test(test_id)
			if 'graph' in test:
				set_test_graph(test_id, test['graph'])
		data = {
			'tests': test_functions(),
			'graphs': graphs()
		}
		return JsonResponse(data)

