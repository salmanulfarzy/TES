from django.contrib import admin

from instructor.models import Courses, Questions, Feedback

admin.site.register(Courses)
admin.site.register(Questions)
admin.site.register(Feedback)
