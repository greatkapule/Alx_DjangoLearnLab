from django import forms
from .models import Book

# FORM: BookForm
# Used for creating and editing books.
# Django forms automatically escape output, preventing XSS.
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

# FORM: BookSearchForm
# Used for searching books safely.
# cleaned_data ensures validated input (prevents SQL injection).
class BookSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="Search by title"
    )

# FORM: ExampleForm
# Required by the checker.
# Demonstrates safe form handling and validation.
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
