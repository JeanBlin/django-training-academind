from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name}'



class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    # author = models.CharField(max_length=100, null=True)) Replaced to get foreign key in Athor table
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, related_name='books')
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True, editable=False, null=False, db_index=True)

    def __str__(self):
        return f'{self.title} ({self.rating})'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])
    