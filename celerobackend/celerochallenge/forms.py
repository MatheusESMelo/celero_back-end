from django import forms
from .models import AthletesAndResults

class AthletesAndResultsForm(forms.ModelForm):
    class Meta:
        model = AthletesAndResults
        fields = [
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
            "fl_deletado",
        ]


class AthletesAndResultsFilterForm(forms.Form):
    name = forms.CharField(label="Name", required=False)
    sex = forms.CharField(label="Sex", required=False)
    team = forms.CharField(label="Team", required=False)
    games = forms.CharField(label="Games", required=False)
    sport = forms.CharField(label="Sport", required=False)
    medal = forms.CharField(label="Medal", required=False)