from django import forms
from .models import Books
from rest_framework import serializers

class BookForm(forms.ModelForm):
    class Meta:
        model =Books
        fields=('bookCot','book_name','book_desc','book_price','location','book_image')


class BookAPIForm(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"