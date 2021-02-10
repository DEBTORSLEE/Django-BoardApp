from django.db import models

# Create your models here.
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    born = models.CharField(max_length=100)
    hp = models.CharField(max_length=100)
    wdate = models.DateTimeField(auto_now_add=True)
    def __str_(self):
        return self.name
        