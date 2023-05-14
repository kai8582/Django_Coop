from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ToDos(models.Model):
    content = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, default = '')



    

