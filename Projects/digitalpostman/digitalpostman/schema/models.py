from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class SchemaItem(models.Model):

    username = models.ForeignKey(User,  on_delete = models.CASCADE)
    schemaname = models.CharField(max_length=100, blank=True)
    changelog = models.TextField(max_length=300, blank=True)
    changedfields = models.CharField(max_length=500, blank=True)
    schemafile = models.FileField(default='sample.txt', upload_to="schemas")

    def __str__(self):
        return self.schemaname

    def content_file_name(instance, filename):
        return '/'.join(['schemas', instance.id, filename])

    def get_absolute_url(self):
        return reverse("schema-detail", kwargs={"pk": self.pk})
    
