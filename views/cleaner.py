from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from ..util.display import test_functions, graphs

@method_decorator(csrf_exempt, name="dispatch")
class CleanerDashboard(View):

    def get(self, request):
        data = {
		'tests': test_functions(),
		'graphs': graphs()
        }
        return JsonResponse(data)

    def post(self, request):
        state = {
        }
        data = {}
        return JsonResponse(data)

