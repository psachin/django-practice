# Create your models here.
from django.db import models
from django.forms import ModelForm

TITLE_CHOICE = (
    ('Mr.','MR'),
    ('Mrs.','MRS'),
    ('Ms.','MS'),
    )

class Author(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICE)
    name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True, auto_now_add=False)

    def __unicode__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.authors

# class AuthorForm(ModelForm):
#     class Meta:
#         model = Author

# class BookForm(ModelForm):
#     class Meta:
#         model = Book


