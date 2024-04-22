from django.urls import path
from .views import UniversityModelViewSet, SponsorModelGenerics, SponsorDetailGenerics, StudentModelGenerics, \
    StudentCreateModelGenerics, StudentUpdateModelGenerics, StudentAddSponsorModelGenerics, SponsorCreate, StudentSponsorView

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'sponsor', SponsorModelViewSet)
router.register(r'university', UniversityModelViewSet)
# router.register(r'student', StudentModelViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('sponsors/list/', SponsorModelGenerics.as_view(), name='sponsors_list'),
    path('sponsor/create/', SponsorCreate.as_view(), name='sponsor_create'),
    path('sponsor/detail/<int:pk>/', SponsorDetailGenerics.as_view(), name='sponsor_detail'),
    path('students/list/', StudentModelGenerics.as_view(), name='students_list'),
    path('student/create/', StudentCreateModelGenerics.as_view(), name='student_create'),
    path('student/detail/<int:pk>/', StudentUpdateModelGenerics.as_view(), name='student_detail'),
    path('student/detail/<int:pk>/addsponsor/', StudentAddSponsorModelGenerics.as_view(), name='student_detail_addsponsor'),
    path('dashboard/', StudentSponsorView.as_view(), name='student_detail_sponsor'),
]
