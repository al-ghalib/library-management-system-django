from django.db import models
# from django.contrib.auth.models import User
from authentication.models import CustomUser as User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    availability_status = models.BooleanField(default=True)
    borrower = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    borrow_date = models.DateField(null=True, blank=True)
    return_deadline = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
