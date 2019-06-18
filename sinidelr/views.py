from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import (
    CreateView,
    ListView,
    DetailView
)
from sinidelr.models import Persona


def index(request):
    return HttpResponse("Hello, world. You're at the people index.")


class PersonaList(ListView):
    model = Persona

class PersonaDetail(DetailView):
    model = Persona