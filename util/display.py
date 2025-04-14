from arches.app.models.models import GraphModel
from importlib import import_module
from inspect import getmembers, isfunction
from cleaner.models import CleanerTest
import os

def test_functions():

	function_module = 'cleaner.functions'

	ret = []
	icons = {}
	mod = import_module(function_module)
	for g in GraphModel.objects.all():
		icons[str(g.pk)] = str(g.iconclass)
	for f in getmembers(mod, isfunction):
		try:
			test = CleanerTest.objects.get(function_module=function_module, function_name=f[0])
		except:
			test = CleanerTest(function_module=function_module, function_name=f[0], enabled=False, graph_id=None)
			test.save()
		icon = 'fa fa-list-alt'
		doc = ''
		if f[1].__doc__:
			doc = str(f[1].__doc__)
		ret.append({'test_id': str(test.test_id), 'function': test.function_name, 'description': doc, 'enabled': test.enabled, 'graph': str(test.graph_id), 'passed': test.test_passed_count, 'failed': test.test_failed_count, 'icon_class': icon, 'results': test.summary})

	return ret

def graphs():

	ret = []
	for g in GraphModel.objects.all():
		if g.name == 'Arches System Settings':
			continue
		ret.append({'graphid': str(g.pk), 'name': str(g.name)})
	return ret
