from django.db import models

# Create your models here.
class Register(models.Model):
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username


class Blog(models.Model):
    title=models.CharField(max_length=80)
    content=models.CharField(max_length=1000)
    username=models.ForeignKey(Register,on_delete=models.CASCADE)

    def __str__(self):
        return self.title