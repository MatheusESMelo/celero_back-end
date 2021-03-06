import random
import factory

from celerochallenge import models


class AthletesAndResultsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.AthletesAndResults
        django_get_or_create = ("pk_athlete",)

    pk_athlete = factory.Faker("pyint")
    
    name = factory.Faker("name")
    sex = "F"
    age = factory.Faker("pyfloat", min_value=15, max_value=60)
    height = factory.Faker("pyfloat", min_value=100, max_value=215)
    weight = factory.Faker("pyfloat", min_value=40, max_value=250)
    team = factory.Faker("country")
    noc = factory.Faker("pystr")
    games = factory.Faker("pystr")
    year = factory.Faker(provider="random_int")
    season = "Summer"
    city = factory.Faker("city")
    sport = factory.Faker("name")
    event = factory.Faker("name")
    medal = "Gold"