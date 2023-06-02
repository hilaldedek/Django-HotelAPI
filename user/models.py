from django.db import models
from django.contrib.auth.models import User




class Customer(models.Model):
     GENDER=(
        ('F','Female'),
        ('M','Male'),
        ('-','Prefer not to say'),
    )
     AGE=(
        ('ucretsiz','0-12'),
        ('tam','12-65'),
        ('%50 indirimli','65+'),
     )
     created=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     name=models.CharField(max_length=32)
     surname=models.CharField(max_length=32)
     user_age=models.CharField(choices=AGE,max_length=16,null=True)
     gender=models.CharField(choices=GENDER,max_length=1,null=True)
     def __str__(self):
          return f'{self.name} - {self.age}'
