from django.urls import re_path
from django.conf import settings
from cleaner.views.cleaner import CleanerDashboard, CleanerReportView

uuid_regex = settings.UUID_REGEX

urlpatterns = [
    re_path(r"^cleaner/", CleanerDashboard.as_view(), name="cleaner"),
    re_path(
        r"^test-report/(?P<resourceid>%s)$" % uuid_regex,
        CleanerReportView.as_view(),
        name="test_report",
    ),
]
