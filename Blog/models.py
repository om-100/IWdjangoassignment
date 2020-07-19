from django.db import models


class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(Timestamp):
    Title = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Title


class Author(Timestamp):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
