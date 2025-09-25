from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from calendar import monthrange
from .models import Event

# Create your views here.
class RegisterView(CreateView):
    template_name = 'authentication/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'authentication/edit_profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class HomePageView(TemplateView):
    template_name = 'authentication/home_page.html'

class CalendarView(TemplateView):
    template_name = 'authentication/calendar.html'

class CalendarView(TemplateView):
    template_name = "calendar.html"

    def get_context_data(self, **kwargs):
        from datetime import date
        context = super().get_context_data(**kwargs)

        year = 2025  # можна зробити динамічним
        months = [
            "Січень", "Лютий", "Березень", "Квітень",
            "Травень", "Червень", "Липень", "Серпень",
            "Вересень", "Жовтень", "Листопад", "Грудень"
        ]

        calendar_data = []
        for month_num in range(1, 13):
            days_in_month = monthrange(year, month_num)[1]

            events = Event.objects.filter(date__year=year, date__month=month_num)
            event_days = {event.date.day: event.title for event in events}

            days = []
            for day in range(1, days_in_month + 1):
                days.append({
                    "number": day,
                    "has_event": day in event_days,
                    "event_title": event_days.get(day, "")
                })

            calendar_data.append({
                "name": months[month_num - 1],
                "days": days
            })

        context["year"] = year
        context["calendar_data"] = calendar_data
        return context