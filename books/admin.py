from django.contrib import admin
from .models import Book, Category, ISBN, Tag
from .forms import BookForm
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    form = BookForm
    list_display = ("title","creator","description")
    list_filter = ("category", )
    search_fields = ("title", )

class BookInLine(admin.StackedInline):
    model = Book
    max_num = 3
    extra = 1

class TagAdmin(admin.ModelAdmin):
    inlines = [BookInLine]


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(ISBN)
admin.site.register(Tag, TagAdmin)
