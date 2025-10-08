from django.urls import path

from .views import PortfolioListView, PortfolioCreateView, PortfolioDetailView, PortfolioDeleteView, LikesAddView

urlpatterns = [
    path("portfolio_list/", PortfolioListView.as_view(),name="port_list"),
    path("portfolio_create/", PortfolioCreateView.as_view(),name="port_create"),
    path("<int:pk>/portfolio_detail/", PortfolioDetailView.as_view(),name="port_detail"),
    path("<int:pk>/portfolio_delete/", PortfolioDeleteView.as_view(),name="port_delete"),
    path("<int:pk>/like",LikesAddView,name="like"),
    
]