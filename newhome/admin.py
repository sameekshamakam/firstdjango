from django.contrib import admin
from newhome.models import Book,Author,Publication,Student

# Register your models here.
#admin.site.register(Book)
#admin.site.register(Author)
#admin.site.register(Publication)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    search_fields=('id','name')
    fields=(('name','purchase_date'),('book_author'))
    list_filter=('name','purchase_date',('book_author',admin.RelatedOnlyFieldListFilter))

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass
