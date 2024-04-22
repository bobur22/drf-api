from django.urls import path, re_path
from .views import AuthorsModelViewSet, BookModelViewSet, BookAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', AuthorsModelViewSet)
router.register(r'books', BookModelViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('book/list/', BookAPIView.as_view(), name='books_list'),
    # re_path('^books/(?P<username>.+)/$', BooksViewSet.as_view()),
]
