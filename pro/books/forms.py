from django.forms.models import modelform_factory, modelformset_factory
from models import Book, Author


BookForm = modelform_factory(Book)
AuthorFormSet = modelformset_factory(Author)


