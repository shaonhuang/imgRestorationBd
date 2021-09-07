from django.db import models

# Create your models here.
class File(models.Model):
    f_filename = models.CharField(max_length=200)
    f_upload_date = models.DateTimeField(auto_now_add=True)
