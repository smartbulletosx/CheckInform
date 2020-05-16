from django.db import models

from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.ImageField(upload_to='image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)