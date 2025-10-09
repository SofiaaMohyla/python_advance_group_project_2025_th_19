from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import RegisterView, ProfileUpdateView, HomePageView, CalendarView, EventCreateView, EventDetailView, EventDeleteView, EventUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('register/', RegisterView.as_view(), name='register'),

    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('profile/', ProfileUpdateView.as_view(), name='profile'),

    path('calendar/<int:year>/<int:month>/', CalendarView.as_view(), name="calendar"),

    path("calendar/add/", EventCreateView.as_view(), name="event_add"),

    path("calendar/event/<int:pk>/", EventDetailView.as_view(), name="event_detail"),

    path('event/<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('event/<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),

]