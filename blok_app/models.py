from django.db import models

# Create your models here.

class Maqola(models.Model):
  sarlavha=models.CharField(("sarlavha"), max_length=50)
  sana=models.DateField()
  maqola=models.TextField(max_length=1000)
  rasm=models.FileField()
  
  def __str__(self) -> str:
    return self.sarlavha
  
class Intert(models.Model):
  sarlavha=models.ForeignKey(Maqola,on_delete=models.CASCADE)
  sana=models.DateField()
  vedio=models.URLField(max_length=200)
  
  def __dir__(self):
    return self.sarlavha