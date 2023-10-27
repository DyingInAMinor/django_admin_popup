from django.db import models

# Create your models here.


class MyCustomModel(models.Model):
    my_custom_field = models.CharField(max_length=256)
    my_custom_file_field = models.FileField(upload_to="files", null=True, blank=True)

    def __str__(self):
        return self.my_custom_field
