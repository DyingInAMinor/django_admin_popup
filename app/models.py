from django.db import models

# Create your models here.


class MyCustomModel(models.Model):
    my_custom_field = models.CharField(max_length=256)

    def __str__(self):
        return self.my_custom_field
