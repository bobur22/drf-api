from django.contrib import admin
from .models import *

admin.site.register(StudentModel)
admin.site.register(CourseModel)
admin.site.register(ModuleModel)
admin.site.register(GradesModel)
admin.site.register(ClassModel)
admin.site.register(AttendanceLogModel)
