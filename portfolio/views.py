from django.shortcuts import render
from .models import Portfolio
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView
from .forms import PortForm
# Create your views here.

class PortfolioListView(ListView):
    model = Portfolio
    template_name="portfolio/portlist.html"
    context_object_name = "prlist"


class PortfolioCreateView(CreateView):
    model = Portfolio
    form_class = PortForm
    template_name = "portfolio/portcreate.html"
    success_url = reverse_lazy("port_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.likes = 0
        return super().form_valid(form)

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio/portdetail.html"
    context_object_name = "prdetail"

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name = ""
    success_url = reverse_lazy("port_list")