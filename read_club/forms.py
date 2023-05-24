from django import forms
from read_club.models import Subscribe, Note, Review


class SubscribeForm(forms.ModelForm):
    """ Форма создания подписки. """
    class Meta:
        model = Subscribe
        fields = ('event',)


class NoteForm(forms.ModelForm):
    """ Форма создания и изменения заметок. """
    class Meta:
        model = Note
        exclude = ('user',)


class ReviewForm(forms.ModelForm):
    """ Форма создания и обновления рецензии. """
    class Meta:
        model = Review
        exclude = ('is_approve', 'user')
