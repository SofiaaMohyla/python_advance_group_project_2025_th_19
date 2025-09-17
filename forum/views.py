from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView,DeleteView
from .models import Branch, Massage
from .forms import BranchCreateForm, MassageCreateForm
# Create your views here.

class BranchCreateView(CreateView):
    model = Branch
    template_name = "forum/branchcreate.html"
    form_class = BranchCreateForm

class BranchListView(ListView):
    model = Branch
    template_name = "forum/branchlist.html"

class MassageCreateView(CreateView):
    model = Massage
    template_name = "forum/massagecreate.html"
    form_class = MassageCreateForm

class MassageListView(ListView):
    model = Massage
    template_name = "forum/massagelist.html"
