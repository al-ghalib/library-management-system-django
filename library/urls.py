from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, BorrowBookView, ReturnBookView

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('borrow/<int:pk>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:pk>/', ReturnBookView.as_view(), name='return-book'),
]
