from django.contrib import admin

from instructor.models import Users, Roles, Classes, Courses

admin.site.register(Users)
admin.site.register(Roles)
admin.site.register(Classes)
admin.site.register(Courses)
