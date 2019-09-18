from django.db import models
from accounts.models import Signup
# Create your models here.
class BookCot(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Location(models.Model):
    hn=models.CharField(max_length=200)
    pincode = models.IntegerField(max_length=6)
    address=models.CharField(max_length=250)

    def __str__(self):
        return self.hn

class Books(models.Model):
    bookCot =models.ForeignKey(BookCot, on_delete=models.CASCADE)
    book_name =models.CharField(max_length=200)
    book_desc =models.TextField()
    book_date=models.DateTimeField(auto_now_add=True)
    book_image = models.ImageField(upload_to='Books', default='bk.png')
    book_user=models.ForeignKey(Signup, on_delete=models.CASCADE)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    book_price =models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.book_name
