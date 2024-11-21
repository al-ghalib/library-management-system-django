from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAdminUser
from datetime import timedelta, date

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class BorrowBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        if not book.availability_status:
            return Response({"error": "Book is not available"}, status=400)
        
        user_borrowed_books = Book.objects.filter(borrower=request.user).count()
        if user_borrowed_books >= 5:
            return Response({"error": "Borrow limit exceeded"}, status=400)

        book.availability_status = False
        book.borrower = request.user
        book.borrow_date = date.today()
        book.return_deadline = date.today() + timedelta(days=14)
        book.save()

        return Response({"message": "Book borrowed successfully!"})

class ReturnBookView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        book = Book.objects.get(pk=pk)
        if book.borrower != request.user:
            return Response({"error": "You cannot return a book you didn't borrow"}, status=400)

        book.availability_status = True
        book.borrower = None
        book.borrow_date = None
        book.return_deadline = None
        book.save()

        return Response({"message": "Book returned successfully!"})
