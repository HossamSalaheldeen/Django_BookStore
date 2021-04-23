from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
import uuid


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50 , validators=[MinLengthValidator(2)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class ISBN(models.Model):
    #isbn_number = models.UUIDField(default = uuid.uuid4,editable=False)
    isbn_number = models.AutoField(primary_key=True)
    author_title = models.CharField(max_length=50, null=True, blank=True)
    book_title = models.CharField(max_length=50, null=True, blank=True)
    

    def __str__(self):
        return f"{self.isbn_number}"
class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="books")
    category = models.ManyToManyField(Category)
    isbn = models.OneToOneField(ISBN, on_delete=models.CASCADE ,null=True, blank=True)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

