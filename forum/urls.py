from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import BranchCreateView, BranchListView, MassageCreateView, MassageListView,MassageDeleteView,MassageUpdateView,BranchDeleteView,BranchUpdateView

urlpatterns = [
    path('create_branch/', BranchCreateView.as_view(), name='create_branch'),
    path('list_branch/', BranchListView.as_view(), name='list_branch'),
    path('<int:pk>/create_massage/', MassageCreateView.as_view(), name='create_massage'),
    path('<int:pk>/list_masage/', MassageListView.as_view(), name='list_masage'),
    path('<int:pk>/deletem',MassageDeleteView.as_view(), name="del_massage"),
    path('<int:pk>/updm',MassageUpdateView.as_view(), name="upd_massage"),
    path('<int:pk>/updb',BranchUpdateView.as_view(), name="upd_branch"),
    path('<int:pk>/deleteb',BranchDeleteView.as_view(), name="del_branch"),
]