from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid

class Migration(migrations.Migration):

	initial = True

	dependencies = [
		migrations.swappable_dependency(settings.AUTH_USER_MODEL),
	]

	forward = "INSERT INTO plugins (pluginid, name, icon, component, componentname, config, slug, sortorder) VALUES ('9ec5b23e-47e8-4c50-a20c-07c98a43f793', '{\"en\": \"Cleaner\"}', 'fa fa-trash', 'views/components/plugins/cleaner', 'cleaner', '{\"show\": true, \"is_workflow\": false, \"description\": \"\"}', 'cleaner', '1' );"

	reverse = "DELETE FROM plugins where pluginid = '9ec5b23e-47e8-4c50-a20c-07c98a43f793';"

	operations = [
		migrations.RunSQL(forward, reverse),
		migrations.CreateModel(
			name='CleanerTest',
			fields=[
				('test_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
				('function_module', models.CharField(max_length=255)),
				('function_name', models.CharField(max_length=255)),
				('graph_id', models.UUIDField(blank=True, null=True)),
				('enabled', models.BooleanField(default=False)),
				('created_time', models.DateTimeField(auto_now_add=True)),
				('updated_time', models.DateTimeField(auto_now=True)),
			],
			options={
				'verbose_name': 'test',
				'verbose_name_plural': 'tests',
				'db_table': 'cleaner_tests',
				'managed': True,
			},
		),
		migrations.CreateModel(
			name='CleanerTestEvent',
			fields=[
				('event_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
				('test_passed_count', models.IntegerField()),
				('test_failed_count', models.IntegerField()),
				('created_time', models.DateTimeField(auto_now_add=True)),
				('updated_time', models.DateTimeField(auto_now=True)),
				('function_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='cleaner.cleanertest')),
				('run_as_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_events', to=settings.AUTH_USER_MODEL)),
			],
			options={
				'verbose_name': 'test run event',
				'verbose_name_plural': 'test run events',
				'db_table': 'cleaner_test_events',
				'managed': True,
			},
		),
		migrations.CreateModel(
			name='CleanerTestResult',
			fields=[
				('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
				('subject_resource', models.UUIDField()),
				('test_result', models.BooleanField(default=False)),
				('created_time', models.DateTimeField(auto_now_add=True)),
				('updated_time', models.DateTimeField(auto_now=True)),
				('function_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='cleaner.cleanertest')),
				('run_as_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results', to=settings.AUTH_USER_MODEL)),
				('test_event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='test_results', to='cleaner.cleanertestevent')),
			],
			options={
				'verbose_name': 'test result',
				'verbose_name_plural': 'test results',
				'db_table': 'cleaner_test_results',
				'managed': True,
			},
		),
	]
