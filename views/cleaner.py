from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from arches.app.views.base import MapBaseManagerView
from arches.app.models.graph import Graph

from ..util.display import test_functions, graphs
from ..util.conf import enable_test, disable_test, set_test_graph
from ..models import CleanerTestEvent

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

class CleanerReportView(MapBaseManagerView):
	def get(self, request, resourceid=None):
		try:
			resource = CleanerTestEvent.objects.only("event_id").get(pk=resourceid)
		except Resource.DoesNotExist:
			raise Http404(_("Test report does not exist"))

		context = self.get_context_data(
			main_script="views/components/plugins/report",
			resourceid=resourceid,
		)

		if resource.function_run.graph_id:
			graph = Graph.objects.get(graphid=resource.function_run.graph_id)
			if graph.iconclass:
				context["nav"]["icon"] = graph.iconclass
			context["nav"]["title"] = graph.name
			context["nav"]["res_edit"] = True
			context["nav"]["print"] = True

		context['report'] = resource

		return render(request, "views/components/plugins/report.htm", context)
