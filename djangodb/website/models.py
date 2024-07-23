from django.db import models

class obituary_platform(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    date_of_death = models.DateField()
    content = models.TextField()
    author = models.CharField(max_length=100)
    submission_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name} ({self.date_of_death})'



