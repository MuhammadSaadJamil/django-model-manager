from django.db import models


# Create your models here.
class Object(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)
    ingredients = models.ManyToManyField('Object', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    display_date = models.DateTimeField(null=True, blank=True)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.name
