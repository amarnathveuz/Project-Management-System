from django.db import models

# Create your models here.


status_type = [
    ("To do","To do"),
    ("Completed","Completed"),
    ("Testing","Testing"),
     ("Onhold","Onhold"),

]

class task(models.Model):
    task_name = models.CharField(max_length=255,null=True)
    status = models.CharField(max_length=50,choices=status_type)