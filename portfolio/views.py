from django.shortcuts import render, get_object_or_404
from .models import Portfolio
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DetailView,DeleteView,UpdateView
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
    template_name = "portfolio/portconfirm.html"
    success_url = reverse_lazy("port_list")

class PortfolioUptadeView(UpdateView):
    model = Portfolio
    
def LikesAddView(request, pk):
    post = get_object_or_404(Portfolio, id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return reverse_lazy("port_list")