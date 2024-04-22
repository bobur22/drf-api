from django.urls import path
# from .views import StudentList, CourseList, ModuleList, GradeList, ClassList, AttendanceList, StudentDetail, AttendanceDetail
from .views import StudentViewSet, ModuleViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
router.register(r'module', ModuleViewSet, basename='module')

urlpatterns = router.urls



# urlpatterns = [
#     path('students/', StudentViewSet.as_view({'get': 'list'})),
#     path('students_create/', StudentViewSet.as_view({'get': 'list', 'post': 'create'})),
#     path('student/<int:pk>/', StudentViewSet.as_view({'get': 'retrieve'})),

#     path('student/list/', StudentList.as_view()),
#     path('student/detail/<int:pk>/', StudentDetail.as_view()),
#     path('course/list/', CourseList.as_view()),
#     path('module/list/', ModuleList.as_view()),
#     path('grade/list/', GradeList.as_view()),
#     path('class/list/', ClassList.as_view()),
#     path('attendance/list/', AttendanceList.as_view()),
#     path('attendance/detail/<int:pk>/', AttendanceDetail.as_view()),
# ]

