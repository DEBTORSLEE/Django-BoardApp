from django.db import models

# Create your models here.
class Board(models.Model):
    board_id = models.AutoField(primary_key=True)
    subj = models.CharField(max_length=200)
    cont = models.TextField(max_length=200)
    hit =  models.IntegerField(default=0)
    wdate = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
                    return self.subj