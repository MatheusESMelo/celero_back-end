"""celerobackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from celerochallenge import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', include('celerochallenge.urls', namespace='celerochallenge'))
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
