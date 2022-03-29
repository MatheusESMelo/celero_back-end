from django.urls import path
from celerochallenge.views import (
    AthletesAndResultsListViewset,
    AthletesAndResultsCreateViewset,
    AthletesAndResultsUpdateViewset,
)

app_name = "celerochallenge"

urlpatterns = [
    path(
        "athletes-and-results-list/",
        AthletesAndResultsListViewset.as_view(),
        name="athletes_and_results_list",
    ),
    path(
        "athletes-and-results-create/",
        AthletesAndResultsCreateViewset.as_view(),
        name="athletes_and_results_create",
    ),
    path(
        "athletes-and-results-update/<pk_athlete>",
        AthletesAndResultsUpdateViewset.as_view(),
        name="athletes_and_results_update",
    ),
]