from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    client_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank = True)

    def __str__(self):
        return str(self.client_name)


class Project(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100, null=True, blank = True)

    def __str__(self):
        return str(self.project_name)