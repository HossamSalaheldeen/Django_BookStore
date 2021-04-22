from django import forms
from .models import Book
from django.core.exceptions import ValidationError
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) <= 10 or len(title) >= 50 :
            raise ValidationError("The length of a book title is between 10 & 50 characters")
        return title

    def clean(self):
        pass
        # super(BookForm,self).clean()
        # category = self.cleaned_data.get('category')
        # #print(list(category))
        # #print(len(category.query))
        # if len(category) < 2:
        #      raise ValidationError("The minimum length of a category name is 2 characters")

        # return self.changed_data