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
            "city",
            "sport",
            "event",
            "medal",
        ]


class AthletesAndResultsFilterForm(forms.Form):
    # TODO: Escolher parametros do filtro e adicionar no form
    name = forms.CharField(label="Teste", required=False)