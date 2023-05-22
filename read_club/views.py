from django.shortcuts import render
from django.views.generic import ListView, DetailView

from read_club.models import Book, Event, Subscribe


class BookListView(ListView):
    model = Book

    def get_detail_url(self, item: Book) -> str:
        return f"/{self.model.__name__}/{item.id}/"

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['detail_url'] = context['foo_list'].filter(Country=64)
        return context


class BookDetailView(DetailView):
    model = Book


class EventListView(ListView):
    model = Event

    # def get_queryset(self):
    #     queryset = super(EventListView, self).get_queryset
    #     return queryset


class EventDetailView(DetailView):
    model = Event


class SubscribeListView(ListView):
    model = Subscribe


class SubscribeDetailView(DetailView):
    model = Subscribe
