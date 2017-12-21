from django.shortcuts import render

from .models import Questions
from .forms import FeedbackForm


def index(request):
    questions = Questions.objects.all()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FeedbackForm()

    context = {'form': form, 'questions': questions}
    return render(request, 'instructor/index.html', context)
