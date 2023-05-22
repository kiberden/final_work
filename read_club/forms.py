from django import forms


class SubscribeForm(forms.Form):
    event_id = forms.IntegerField(widget=forms.HiddenInput)
    book_id = forms.IntegerField(widget=forms.HiddenInput)

    def subscribe(self):
        # send email using the self.cleaned_data dictionary
        pass
