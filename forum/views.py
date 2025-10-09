from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView,DeleteView,UpdateView
from .models import Branch, Massage
from .forms import BranchCreateForm, MassageCreateForm
from django.urls import reverse_lazy
# Create your views here.

class BranchCreateView(CreateView):
    model = Branch
    template_name = "forum/branchcreate.html"
    form_class = BranchCreateForm
    success_url = reverse_lazy("list_branch")
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BranchListView(ListView):
    model = Branch
    template_name = "forum/branchlist.html"
    context_object_name = "branchlist"

class MassageCreateView(CreateView):
    model = Massage
    template_name = "forum/massagecreate.html"
    form_class = MassageCreateForm
    success_url = reverse_lazy("list_branch")

    def form_valid(self, form):
        form.instance.author = self.request.user
        branch = self.kwargs["pk"]
        form.instance.branch = Branch.objects.get(id=branch)
        return super().form_valid(form)
    
class MassageListView(ListView):
    model = Massage
    template_name = "forum/massagelist.html"
    context_object_name = "massagelist"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['branch'] = self.kwargs["pk"]
        return context
    
    def get_queryset(self):
        branch = self.kwargs["pk"]
        return Massage.objects.filter(branch=branch)

class MassageUpdateView(UpdateView):
    model=Massage
    template_name = "forum/updform.html"
    fields=["massage"]
    success_url = reverse_lazy("list_branch")

class MassageDeleteView(DeleteView):
    model = Massage 
    template_name = "forum/confirmdel.html"
    success_url = reverse_lazy("list_branch")

class BranchDeleteView(DeleteView):
    model = Branch
    template_name = "forum/confirmdel.html"
    success_url = reverse_lazy("list_branch")

class BranchUpdateView(UpdateView):
    model = Branch
    fields = ["name","description"]
    template_name = "forum/updform.html"
    success_url = reverse_lazy("list_branch")