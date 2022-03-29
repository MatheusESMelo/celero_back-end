from django.urls import path
from . import views

app_name = "celerochallenge"

urlpatterns = [
    path(
        "athletes-and-results-list/",
        views.AthletesAndResultsListViewset.as_view(),
        name="athletes_and_results_list",
    ),
    path(
        "athletes-and-results-create/",
        views.AthletesAndResultsCreateViewset.as_view(),
        name="athletes_and_results_create",
    ),
    path(
        "athletes-and-results-update/<pk_athlete>",
        views.AthletesAndResultsUpdateViewset.as_view(),
        name="athletes_and_results_update",
    ),
]