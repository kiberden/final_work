import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView, DetailView, CreateView

from read_club.forms import SubscribeForm, NoteForm, ReviewForm
from read_club.middleware import get_current_user
from read_club.models import Book, Event, Subscribe, Note, Review


class BookListView(ListView):
    """ Представление списка книг. """
    model = Book


class BookDetailView(DetailView):
    """ Детальное представление книги. """
    model = Book


class EventListView(ListView,):
    """ Представление списка событий. """
    model = Event

    def get_queryset(self):
        """ Модифицируем параметр выборк, добавляем фильтр по дате. """
        queryset = super().get_queryset()
        return queryset.filter(finish__gt=datetime.date.today())


class SubscribeListView(ListView):
    """ Представление списка подписок. """
    model = Subscribe

    def get_queryset(self):
        """ Модифицируем параметр выборк, добавляем фильтр по дате. """
        queryset = super().get_queryset()
        return queryset.filter(user=get_current_user()).order_by('-event__finish', )


class SubscribeDetailView(DetailView):
    """ Представление деталки и формы для подписок. """
    model = Subscribe


class SubscribeCreateView(CreateView):
    """ Представление создания подписки. """
    form_class = SubscribeForm
    success_url = '/events/'
    model = Subscribe

    def form_valid(self, form) -> HttpResponse:
        """ При валидации формы прокидываем значение текущего пользователя. """
        form.instance.user = get_current_user()
        form.instance.user_id = get_current_user().id
        return super().form_valid(form)

    def form_invalid(self, form):
        """ Если форма не валидна - редиректим на страницу эвента. """
        return HttpResponseRedirect(self.get_success_url())


class NoteCreateView(CreateView):
    """ Представление обновления и создания заметок. """
    form_class = NoteForm
    success_url = '/subscribes/'
    model = Note

    def form_valid(self, form) -> HttpResponse:
        """ При валидации формы прокидываем значение текущего пользователя. """
        form.instance.user = get_current_user()
        form.instance.user_id = get_current_user().id
        super().form_valid(form)
        subscribe = Subscribe.objects.filter(user=get_current_user(), event=form.instance.event).first()
        return HttpResponseRedirect(f"{self.get_success_url()}{subscribe.id}/")

    def form_invalid(self, form):
        """ Если форма не валидна - редиректим на страницу эвента. """
        subscribe = Subscribe.objects.filter(user=get_current_user(), event=form.instance.event).first()
        return HttpResponseRedirect(f"/{self.get_success_url()}{subscribe.id}/")


class ReviewCreateView(CreateView):
    """ Представление обновления и создания рецензии. """
    form_class = ReviewForm
    success_url = '/subscribes/'
    model = Review

    def form_valid(self, form) -> HttpResponse:
        """ При валидации формы прокидываем значение текущего пользователя. """
        form.instance.user = get_current_user()
        form.instance.user_id = get_current_user().id
        super().form_valid(form)
        subscribe = Subscribe.objects.filter(user=get_current_user(), event=form.data['event']).first()
        return HttpResponseRedirect(f"{self.get_success_url()}{subscribe.id}/")

    def form_invalid(self, form):
        """ Если форма не валидна - редиректим на страницу эвента. """
        subscribe = Subscribe.objects.filter(user=get_current_user(), event=form.data['event']).first()
        return HttpResponseRedirect(f"/{self.get_success_url()}{subscribe.id}/")
