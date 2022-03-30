from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from allauth.account.views import SignupView
from celerochallenge.views import (
    main,
    AthletesAndResultsListViewset,
    AthletesAndResultsCreateViewset,
    AthletesAndResultsUpdateViewset,
)

app_name = "celerochallenge"

urlpatterns = [
    path("", main, name="main"),
    path("login/", LoginView.as_view(template_name="celero/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="celero/logout.html"), name="logout"),
    path("signup/", SignupView.as_view(template_name="celero/signup.html"), name="signup"),
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