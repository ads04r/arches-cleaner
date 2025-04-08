from django.utils.decorators import method_decorator
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from arches.app.models.models import ResourceInstance, TileModel
from django.http import JsonResponse
# from cleaner.models import 

@method_decorator(csrf_exempt, name="dispatch")
class CleanerDashboard(View):

    def get(self, request):
        data = {
        }
        return JsonResponse(data)

    def post(self, request):
        state = {
        }
        data = {}
        return JsonResponse(data)

