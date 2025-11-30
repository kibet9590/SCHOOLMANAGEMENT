from django.contrib import admin

from school.models import Course, Announcement,Trainer

# Register your models here.
admin.site.register(Course)
admin.site.register(Trainer)
admin.site.register(Announcement)
