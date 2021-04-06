from django.db import models
from django.db.models import Model
# Create your models here.

class Link(Model):
    title = models.CharField(max_length=100, verbose_name="Titulo")
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to="links")

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Link"
        verbose_name_plural="Links"

    
    def __str__(self):
        return self.title
    
