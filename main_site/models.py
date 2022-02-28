from django.db import models

class Upload(models.Model):
    _name = models.CharField(max_length=30, null=True)
    _file = models.FileField(null=True, upload_to='media/')