from django.urls import re_path
from cleaner.views.cleaner import CleanerDashboard

urlpatterns = [
    re_path(r"^cleaner/", CleanerDashboard.as_view(), name="cleaner"),
]
