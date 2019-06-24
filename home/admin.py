from django.contrib import admin
from home.models import Book,Author,Publication

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publication)
