from django.contrib import admin
from library.models import (IssuedBook, Member, Book, Author, Publisher,
                            Category, LibraryBranch, City)

# Register your models here.

admin.site.register(IssuedBook)
admin.site.register(Member)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(LibraryBranch)
admin.site.register(City)