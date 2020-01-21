from django.contrib import admin
from .models import teacher
from .models import timetable
from .models import student
from .models import student_marks
# Register your models here.
admin.site.register(teacher)
admin.site.register(timetable)
admin.site.register(student)
admin.site.register(student_marks)