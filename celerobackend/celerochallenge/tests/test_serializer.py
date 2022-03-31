from django.test import TestCase
from django.urls import reverse

from celerochallenge.factories import AthletesAndResultsFactory
from celerochallenge.serializers import AthletesAndResultsSerializer
from django.contrib.auth.models import User


class TestAthletesAndResultsSerializer(TestCase):
    def setUp(self):
        self.athletes_and_results = AthletesAndResultsFactory()
        self.user = User.objects.create_user(username="tester", password="password")
        self.url_generated_from_view_name = reverse(
            "celerochallenge:athletes_and_results_update",
            kwargs={"pk_athlete": self.athletes_and_results.pk_athlete},
        )

    def test_it_returns_the_expected_fields(self):
        serializer = AthletesAndResultsSerializer(self.athletes_and_results)
        data = serializer.data

        update_link = "{url}".format(
            url=self.url_generated_from_view_name
        )

        self.assertEqual(data["name"], self.athletes_and_results.name)
        self.assertEqual(data["sex"], str(self.athletes_and_results.sex))
        self.assertEqual(data["age"], str(self.athletes_and_results.age))
        self.assertEqual(data["height"], str(self.athletes_and_results.height))
        self.assertEqual(data["weight"], str(self.athletes_and_results.weight))
        self.assertEqual(data["team"], self.athletes_and_results.team)
        self.assertEqual(data["noc"], self.athletes_and_results.noc)
        self.assertEqual(data["games"], self.athletes_and_results.games)
        self.assertEqual(data["year"], str(self.athletes_and_results.year))
        self.assertEqual(data["season"], str(self.athletes_and_results.season))
        self.assertEqual(data["city"], self.athletes_and_results.city)
        self.assertEqual(data["sport"], self.athletes_and_results.sport)
        self.assertEqual(data["event"], self.athletes_and_results.event)
        self.assertEqual(data["medal"], str(self.athletes_and_results.medal))
        self.assertEqual(data["update_link"], update_link)
