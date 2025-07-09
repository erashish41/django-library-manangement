from django.contrib.auth.models import User
from django.db import models
from utils.models import BaseMixin


# Create your models here.
class City(BaseMixin):
    city_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.city_name

class LibraryBranch(BaseMixin):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="branches_city")
    phone = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return f"{self.name} - {self.city.city_name}"


class Category(BaseMixin):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Publisher(BaseMixin):
    name = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

    
class Author(BaseMixin):
    name = models.CharField(max_length=100,null=True)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name} - {self.bio}"


class Book(BaseMixin):
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.ManyToManyField(Author,related_name="book_author")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="book_category")
    publisher = models.ForeignKey(Publisher, on_delete=models.SET_NULL, null=True, related_name="book_publisher")
    library_branch = models.ForeignKey(LibraryBranch, on_delete=models.SET_NULL, null=True, related_name="books")
    
    def __str__(self):
        return f"{self.title} - {self.isbn}"
    

class Member(BaseMixin):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="member_profile")
    address = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=15,null=True,blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, related_name="members_city")
    
    def __str__(self):
        return f"{self.user.username} - {self.address}"

    
class IssuedBook(BaseMixin):
    member = models.ForeignKey(Member,on_delete=models.CASCADE,related_name="issued_books")
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,related_name="issued_records")
    
    def __str__(self):
        return f"{self.book.title} - {self.member.user.username}"