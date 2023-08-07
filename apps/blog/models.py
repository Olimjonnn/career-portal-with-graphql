from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(upload_to='media/', null=True, blank=True)

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, null=True, related_name="created", on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(User, null=True, related_name="modified", on_delete=models.SET_NULL)

    def __str__(self):
        return self.title