from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm, EventForm
from calendar import monthrange
from .models import Event
from datetime import date

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
    template_name = "authentication/calendar.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        year = date.today().year
        context['year'] = year

        UKR_MONTHS = {
            1: "Січень",
            2: "Лютий",
            3: "Березень",
            4: "Квітень",
            5: "Травень",
            6: "Червень",
            7: "Липень",
            8: "Серпень",
            9: "Вересень",
            10: "Жовтень",
            11: "Листопад",
            12: "Грудень",
        }

        # Приклад формування даних календаря
        calendar_data = []
        for month_num in range(1, 13):
            month_days = []
            num_days = monthrange(year, month_num)[1]
            for day_num in range(1, num_days + 1):
                events = Event.objects.filter(date=date(year, month_num, day_num))
                if events.exists():
                    event = events.first()
                    month_days.append({
                        'number': day_num,
                        'has_event': True,
                        'event_title': event.title,
                        'event_id': event.id,  # <- важливо!
                    })
                else:
                    month_days.append({
                        'number': day_num,
                        'has_event': False,
                        'event_title': '',
                        'event_id': None,
                    })
            calendar_data.append({
                'name': UKR_MONTHS[month_num],
                'days': month_days
            })

        context['calendar_data'] = calendar_data
        return context

class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = "authentication/calendar_event_add.html"
    success_url = reverse_lazy('calendar')

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['date'].input_formats = ['%Y-%m-%d']
        form.fields['start_time'].input_formats = ['%H:%M']
        form.fields['end_time'].input_formats = ['%H:%M']
        return form

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = "authentication/calendar_event_add.html"
    success_url = reverse_lazy('calendar')


class EventDetailView(DetailView):
    model = Event
    template_name = "authentication/calendar_event_detail.html"


class EventDeleteView(UserPassesTestMixin, DeleteView):
    model = Event
    template_name = "authentication/calendar_event_confirm_delete.html"
    success_url = reverse_lazy('calendar')

    def test_func(self):
        # тільки модератори та адміни можуть видаляти
        return self.request.user.is_authenticated and self.request.user.role in ['moderator', 'admin']
