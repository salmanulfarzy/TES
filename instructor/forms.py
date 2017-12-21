from django import forms
from instructor.models import Feedback


class FeedbackForm(forms.Form):

    class Meta:
        model = Feedback
        fields = 'review'
        widgets = {
            'review': forms.RadioSelect,
        }
