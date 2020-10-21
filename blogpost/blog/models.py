from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    slug = models.SlugField(unique=True, blank=False, null=False)
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.slug