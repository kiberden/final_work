from threading import local

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

_user = local()


class CurrentUserMiddleware(MiddlewareMixin):
    """ Посредник для получения текущего пользователя. """
    def process_request(self, request):
        """ Сохраняем текущего пользователя из запроса. """
        _user.value = request.user


class AuthorizeUserMiddleware(MiddlewareMixin):
    """ Посредник для редиректов польователя. """
    def process_request(self, request):
        url_first_dir = request.path.split('/')[1]

        if request.user.is_anonymous and url_first_dir != 'admin':
            return redirect('/admin/')

        if not request.user.is_superuser and not request.user.is_anonymous and url_first_dir == 'admin':
            return redirect('/books/')


def get_current_user():
    """ Получаем текущего пользователя. """
    try:
        return _user.value
    except AttributeError:
        return None
