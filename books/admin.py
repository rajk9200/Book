from django.contrib import admin

# Register your models here.
from .models import Books,BookCot,Location
admin.site.register(Books)
admin.site.register(BookCot)
admin.site.register(Location)
