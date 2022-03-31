from celerochallenge.models import AthletesAndResults
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from celerochallenge.factories import AthletesAndResultsFactory


class TestAthletesAndResultsList(TestCase):
    def setUp(self):
        self.athletes_and_results = AthletesAndResultsFactory()
        self.user = User.objects.create_user(username="tester", password="password")
        self.url_generated_from_view_name = reverse("celerochallenge:athletes_and_results_list")
        for _ in range(15):
            AthletesAndResultsFactory()

    def test_it_requires_login(self):
        response = self.client.get(reverse("celerochallenge:athletes_and_results_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_it_lists_athletes_with_all_required_fields(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("celerochallenge:athletes_and_results_list"))

        expected_fields = [
            "pk_athlete",
            "name",
            "sex",
            "age",
            "height",
            "weight",
            "team",
            "noc",
            "games",
            "year",
            "season",
            "city",
            "sport",
            "event",
            "medal", 
            "update_link",
        ]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["athletes_and_results_list"]), 10)
        self.assertEqual(
            list(response.context["athletes_and_results_list"][0].keys()).sort(),
            expected_fields.sort(),
        )

    def test_if_filters_for_ten_athletes(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("celerochallenge:athletes_and_results_list"))

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(AthletesAndResults.objects.all()), 10)
        self.assertEqual(len(response.context["athletes_and_results_list"]), 10)

    def test_if_filters_for_athletes_name_when_name_parameter_is_used(self):

        self.client.force_login(self.user)
        url = "{}?name={}".format(
            reverse("celerochallenge:athletes_and_results_list"), self.athletes_and_results.name
        )
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(AthletesAndResults.objects.all()), 1)
        self.assertEqual(len(response.context["athletes_and_results_list"]), 1)
    
    def test_if_filters_for_athletes_sex_when_sex_parameter_is_used(self):

        self.client.force_login(self.user)
        url = "{}?sex={}".format(
            reverse("celerochallenge:athletes_and_results_list"), self.athletes_and_results.sex
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertGreaterEqual(len(AthletesAndResults.objects.all()), 1)
        self.assertGreaterEqual(len(response.context["athletes_and_results_list"]), 1)
    
    def test_if_filters_for_athletes_teams_when_team_parameter_is_used(self):

        self.client.force_login(self.user)
        url = "{}?team={}".format(
            reverse("celerochallenge:athletes_and_results_list"), self.athletes_and_results.team
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(AthletesAndResults.objects.all()), 1)
        self.assertGreaterEqual(len(response.context["athletes_and_results_list"]), 1)
    
    def test_if_filters_for_athletes_games_when_games_parameter_is_used(self):

        self.client.force_login(self.user)
        url = "{}?games={}".format(
            reverse("celerochallenge:athletes_and_results_list"), self.athletes_and_results.games
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(AthletesAndResults.objects.all()), 1)
        self.assertEqual(len(response.context["athletes_and_results_list"]), 1)
    
    def test_if_filters_for_athletes_sport_when_sport_parameter_is_used(self):

        self.client.force_login(self.user)
        url = "{}?sport={}".format(
            reverse("celerochallenge:athletes_and_results_list"), self.athletes_and_results.sport
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(AthletesAndResults.objects.all()), 1)
        self.assertEqual(len(response.context["athletes_and_results_list"]), 1)
    
    def test_if_filters_for_athletes_medals_when_medal_parameter_is_used(self):

        self.client.force_login(self.user)
        url = "{}?medal={}".format(
            reverse("celerochallenge:athletes_and_results_list"), self.athletes_and_results.medal
        )
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(AthletesAndResults.objects.all()), 1)
        self.assertGreaterEqual(len(response.context["athletes_and_results_list"]), 1)


class TestAthletesAndResultsCreate(TestCase):
    def setUp(self):
        self.athletes_and_results = AthletesAndResultsFactory()

        self.user = User.objects.create_user(username="tester", password="password")
        self.url_generated_from_view_name = reverse("celerochallenge:athletes_and_results_create")

    def test_it_requires_login_to_get_the_create_form_page(self):
        response = self.client.get(reverse("celerochallenge:athletes_and_results_create"))

        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_creates_athletes_and_results(self):
        athletes_and_results = AthletesAndResultsFactory()

        data = {
            "pk_athlete": athletes_and_results.pk_athlete,
            "name": athletes_and_results.name,
            "sex": athletes_and_results.sex,
            "age": athletes_and_results.age,
            "height": athletes_and_results.height,
            "weight": athletes_and_results.weight,
            "team": athletes_and_results.team,
            "noc": athletes_and_results.noc,
            "games": athletes_and_results.games,
            "year": athletes_and_results.year,
            "season": athletes_and_results.season,
            "city": athletes_and_results.city,
            "sport": athletes_and_results.sport,
            "event": athletes_and_results.event,
            "medal": athletes_and_results.medal,
        }

        self.client.force_login(self.user)
        self.client.post(self.url_generated_from_view_name, data=data)

        athletes_and_results_from_db = AthletesAndResults.objects.filter(pk_athlete=athletes_and_results.pk_athlete)

        self.assertEqual(len(athletes_and_results_from_db), 1)


class TestAthletesAndResultsUpdate(TestCase):
    def setUp(self):
        self.athletes_and_results = AthletesAndResultsFactory(name="Atleta Nome Antigo")
        self.user = User.objects.create_user(username="tester", password="password")
        self.url_generated_from_view_name = reverse(
            "celerochallenge:athletes_and_results_update",
            kwargs={"pk_athlete": self.athletes_and_results.pk_athlete},
        )

    def test_it_requires_login_to_get_the_update_form_page(self):
        response = self.client.get(
            reverse(
                "celerochallenge:athletes_and_results_update",
                kwargs={"pk_athlete": self.athletes_and_results.pk_athlete},
            )
        )

        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_it_updates_athletes_and_results_record_in_the_database(self):
        updated_name="Atleta Nome Atualizado"

        self.assertNotEqual(
            updated_name, self.athletes_and_results.name
        )

        data = {
            "pk_athlete": self.athletes_and_results.pk_athlete,
            "name": updated_name,
            "sex": self.athletes_and_results.sex,
            "age": self.athletes_and_results.age,
            "height": self.athletes_and_results.height,
            "weight": self.athletes_and_results.weight,
            "team": self.athletes_and_results.team,
            "noc": self.athletes_and_results.noc,
            "games": self.athletes_and_results.games,
            "year": self.athletes_and_results.year,
            "season": self.athletes_and_results.season,
            "city": self.athletes_and_results.city,
            "sport": self.athletes_and_results.sport,
            "event": self.athletes_and_results.event,
            "medal": self.athletes_and_results.medal,
        }

        self.client.force_login(self.user)

        response = self.client.post(self.url_generated_from_view_name, data=data)
        self.assertIn("atualizados com sucesso", response.context["message"])

        refreshed_athletes_and_results = AthletesAndResults.objects.get(
            pk_athlete=self.athletes_and_results.pk_athlete
        )
        self.assertEqual(
            refreshed_athletes_and_results.name, updated_name
        )
