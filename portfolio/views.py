from django.shortcuts import render
from .models import Portfolio
from django.views.generic import CreateView,ListView,DetailView,DeleteView
# Create your views here.

class PortfolioListView(ListView):
    model = Portfolio
    template_name="portfolio/portlist.html"
    context_object_name = "prlist"