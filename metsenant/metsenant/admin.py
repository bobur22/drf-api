from django.contrib import admin
from .models import SponsorModel, UniversitiesModel, StudentModel, SponsorStudentModel, Overall

admin.site.register(SponsorModel)
admin.site.register(UniversitiesModel)
admin.site.register(StudentModel)
admin.site.register(SponsorStudentModel)
admin.site.register(Overall)