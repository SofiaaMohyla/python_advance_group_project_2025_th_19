from django.shortcuts import render, get_object_or_404, redirect
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
        return super().form_valid(form)

class PortfolioDetailView(DetailView):
    model = Portfolio
    template_name = "portfolio/portdetail.html"
    context_object_name = "prdetail"

    def get_context_data(self, *args, **kwargs):
        context = super(PortfolioDetailView, self).get_context_data()
        stuff = get_object_or_404(Portfolio, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class PortfolioDeleteView(DeleteView):
    model = Portfolio
    template_name = "portfolio/portconfirm.html"
    success_url = reverse_lazy("port_list")

class PortfolioUptadeView(UpdateView):
    model = Portfolio
    
def LikesAddView(request, pk):
    post = get_object_or_404(Portfolio, id=request.POST.get('like_id'))
    post.likes.add(request.user)
    return redirect("port_list")