from django.urls import path

from read_club import views

urlpatterns = [
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),

    path('events/', views.EventListView.as_view()),
    path('events/<int:pk>', views.EventDetailView.as_view()),

    path('subscribes/', views.SubscribeListView.as_view())
]
