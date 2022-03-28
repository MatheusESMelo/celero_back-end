from django.urls import reverse
from rest_framework import serializers


class AthletesAndResultsSerializer(serializers.Serializer):
    name = serializers.CharField()
    sex = serializers.CharField()
    age = serializers.CharField()
    height = serializers.CharField()
    weight = serializers.CharField()
    team = serializers.CharField()
    noc = serializers.CharField()
    games = serializers.CharField()
    year = serializers.CharField()
    season = serializers.CharField()
    city = serializers.CharField()
    sport = serializers.CharField()
    event = serializers.CharField()
    medal = serializers.CharField()
    update_link = serializers.SerializerMethodField()

    def get_update_link(self, instance):
        update_link = "{url}".format(
            url=reverse(
                "celerochallenge:athletes_and_results_update",
                kwargs={"pk_athlete": instance.pk_athlete},
            ),
        )

        return update_link