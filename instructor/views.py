from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import FeedbackForm


def index(request):
    if request.method == 'POST':
        #  create a form instance and populate it with request data
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # process the data in form as required
            return HttpResponseRedirect('/')
    else:
        form = FeedbackForm()

    return render(request, 'instructor/index.html', {'form': form})
