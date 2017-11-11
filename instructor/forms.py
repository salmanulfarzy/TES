from django import forms

RADIO_CHOICE = [ (i, i) for i in range(1,9) ]

class FeedbackForm(forms.Form):
    comments = forms.CharField(widget=forms.Textarea)
    radio = forms.ChoiceField(widget=forms.RadioSelect(), choices=RADIO_CHOICE)
