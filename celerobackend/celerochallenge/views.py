from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from rest_framework import generics
from .forms import (
    AthletesAndResultsForm,
    AthletesAndResultsFilterForm,
)

from .models import AthletesAndResults
from .serializers import AthletesAndResultsSerializer
from .mixins import ListModelMixin



class AthletesAndResultsListViewset(
    LoginRequiredMixin, ListModelMixin, generics.GenericAPIView
):

    queryset = AthletesAndResults.objects.filter()
    serializer_class = AthletesAndResultsSerializer
    template_name = "athletes_and_results.html"

    def filter_queryset(self, queryset):

        # TODO: Escolher os parametros do filtro

        filtro_teste = self.request.GET.get("name")

        queryset = queryset.order_by("-pk_athlete")

        # TODO: Incluir if e else para os futuros parametros do filtro
        if not (filtro_teste):
            queryset = queryset[:10]
        else:
            if filtro_teste:
                queryset = queryset.filter(name__icontains=filtro_teste)

        return queryset

    def get(self, request, *args, **kwargs):
        athletes_and_results_list = self.list(request, *args, **kwargs)

        context = {
            "athletes_and_results_list": athletes_and_results_list,
            # TODO: Adicionar form para o filtro
            #"filters_form": AthletesAndResultsFilterForm(),
        }

        return render(request, self.template_name, context=context)


class AthletesAndResultsUpdateViewset(LoginRequiredMixin, generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        pk_athlete = kwargs.get("pk_athlete")

        athletes_and_results_data = AthletesAndResults.objects.get(pk_athlete=pk_athlete)

        athletes_and_results_form = AthletesAndResultsForm(
            initial={
                "pk_athlete": athletes_and_results_data.pk_athlete,
                "name": athletes_and_results_data.name,
                "sex": athletes_and_results_data.sex,
                "age": athletes_and_results_data.age,
                "height": athletes_and_results_data.height,
                "weight": athletes_and_results_data.weight,
                "team": athletes_and_results_data.team,
                "noc": athletes_and_results_data.noc,
                "games": athletes_and_results_data.games,
                "year": athletes_and_results_data.year,
                "season": athletes_and_results_data.season,
                "city": athletes_and_results_data.city,
                "sport": athletes_and_results_data.sport,
                "event": athletes_and_results_data.event,
                "medal": athletes_and_results_data.medal,
            }
        )

        context = {"athletes_and_results_form": athletes_and_results_form, "message": ""}

        return render(request, "flux/pessoa_fisica_create_update.html", context=context)

    def post(self, request, *args, **kwargs):
        pk_athlete = kwargs.get("pk_athlete")
        athletes_and_results = AthletesAndResults.objects.get(pk_athlete=pk_athlete)
        athletes_and_results_form = AthletesAndResultsForm(request.POST, instance=athletes_and_results)

        if athletes_and_results_form.is_valid():
            athletes_and_results_form.save()

            message = "Dados do atleta {} atualizados com sucesso".format(
                athletes_and_results.name
            )
        else:
            message = "Erro ao atualizar os dados do atleta {}, confira os dados e tente novamente".format(
                athletes_and_results.name
            )

            for field, error_message in athletes_and_results_form.errors.items():
                form_error_message = (
                    "Erro ao atualizar atleta. Campo: {}; Erro: {}".format(
                        field, error_message
                    )
                )

        context = {"athletes_and_results_form": athletes_and_results_form, "message": message}

        return render(request, "athletes_and_results_create_update.html", context=context)


class AthletesAndResultsCreateViewset(LoginRequiredMixin, generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        athletes_and_results_form = AthletesAndResultsForm()

        context = {"athletes_and_results_form": athletes_and_results_form, "message": ""}

        return render(request, "athletes_and_results_create_update.html", context=context)

    def post(self, request, *args, **kwargs):
        message = ""
        athletes_and_results_form = AthletesAndResultsForm(request.POST)

        if athletes_and_results_form.is_valid():
            athletes_and_results_instance = athletes_and_results_form.save(commit=False)

            athletes_and_results_instance.save()

            message = "Atleta criado com sucesso"

        context = {"athletes_and_results_form": athletes_and_results_form, "message": message}

        return render(request, "athletes_and_results_create_update.html", context=context)