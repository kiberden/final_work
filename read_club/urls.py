from django.urls import path

from read_club import views

urlpatterns = [
    path('books/', views.BookListView.as_view()),
    path('books/<int:pk>/', views.BookDetailView.as_view()),

    path('events/', views.EventListView.as_view()),

    path('subscribes/', views.SubscribeListView.as_view()),
    path('subscribes/<int:pk>/', views.SubscribeDetailView.as_view()),
    path('subscribes/create/', views.SubscribeCreateView.as_view(http_method_names=['post'])),

    path('notes/create/', views.NoteCreateView.as_view(http_method_names=['post'])),
    path('reviews/create/', views.ReviewCreateView.as_view(http_method_names=['post']))
]
