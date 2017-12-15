from django import forms

RADIO_CHOICE = [
    (2, 'Very Good'), (1, 'Good'), (0, 'Okay'),
    (-1, 'Bad'), (-2, 'Very Bad')
]


class FeedbackForm(forms.Form):
    review = forms.ChoiceField(widget=forms.RadioSelect(),
                               label='Question',
                               choices=RADIO_CHOICE)
