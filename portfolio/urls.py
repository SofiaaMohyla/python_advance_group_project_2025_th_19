from django.urls import path
from .views import PortfolioListView
urlpatterns = [
    path("portfolio_list/", PortfolioListView.as_view(),name="port_list"),
]