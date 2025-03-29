from django.db import models
from django.core.validators import MinValueValidator

class HelloEntry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[MinValueValidator(18)])
    is_student= models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)