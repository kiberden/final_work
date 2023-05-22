import datetime
from time import timezone

from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView

from read_club.forms import SubscribeForm, NoteForm, ReviewForm
from read_club.models import Book, Event, Subscribe, Note, Review


class BookListView(ListView):
    """ Представление списка книг. """
    model = Book

    # def get_detail_url(self, item: Book) -> str:
    #     """ Получаем сслку на детальный элемент. """
    #     return f"/{self.model.__name__}/{item.id}/"

    # def get_context_data(self, **kwargs):
    #     """"""
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # context['detail_url'] = context['foo_list'].filter(Country=64)
    #     return context


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


class SubscribeDetailView(DetailView):
    """ Представление деталки и формы для подписок. """
    model = Subscribe


class SubscribeCreateView(CreateView):
    """ Представление создания подписки. """
    form_class = SubscribeForm
    success_url = '/events/'
    model = Subscribe

    def form_valid(self, form):
        """ Добавление данных перед валидацией формы."""
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteCreateView(CreateView):
    """ Представление обновления и создания заметок. """
    form_class = NoteForm
    success_url = '/subscribes/'
    model = Note


class ReviewCreateView(CreateView):
    """ Представление обновления и создания рецензии. """
    form_class = ReviewForm
    success_url = '/subscribes/'
    model = Review
