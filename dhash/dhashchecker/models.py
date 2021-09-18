from django.db import models

# Create your models here.
class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100)
    file_hash = models.CharField(max_length=50)
    repos = models.TextField()
    repo_count = models.IntegerField()