from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import BranchCreateView, BranchListView, MassageCreateView, MassageListView

urlpatterns = [
    path('create_branch/', BranchCreateView.as_view(), name='create_branch'),
    path('list_branch/', BranchListView.as_view(), name='list_branch'),
    path('<int:pk>/create_massage/', MassageCreateView.as_view(), name='create_massage'),
    path('<int:pk>/list_masage/', MassageListView.as_view(), name='list_masage'),
]