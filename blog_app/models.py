from django.db import models

# Create your models here.
class ShowData(models.Model):
    name=models.CharField(max_length=100)
    post=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+str(self.date)
    
    class Meta:
        ordering=['-date']