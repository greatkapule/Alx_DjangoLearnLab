from django.db import models

class Author(models.Model):
    #One Author -> Many Books (one-to-many relationship)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    #Each book belongs to one Author
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
