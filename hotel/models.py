from django.db import models
from django.contrib.auth.models import User

class Rezervation(models.Model):
    CITY=(
        (1,'Antalya'),
        (2,'Izmir'),
        (3,'Istanbul'),
        (4,'Fethiye'),
        (5,'Bodrum'),
        (6,'Datça'),
        (7,'Urla'),
    )
    vacation=models.IntegerField(choices=CITY)
    start_date=models.DateField()
    finish_date=models.DateField()
    visitor_number=models.IntegerField()
    def __str__(self):
        return f'{self.vacation} --> {self.visitor_number}'
    
class RezervationDetail(models.Model):
    GENDER=(
        ('F','Female'),
        ('M','Male'),
        ('-','Prefer not to say'),
    )
    AGE=(
        ('ucretsiz','0-12'),
        ('tam bilet','12-65'),
        ('%50 indirimli','65+'),
     )
    detail=models.OneToOneField(Rezervation,on_delete=models.CASCADE)
    name=models.CharField(max_length=32)
    surname=models.CharField(max_length=32)
    user_age=models.CharField(choices=AGE,max_length=16,null=True)
    gender=models.CharField(choices=GENDER,max_length=1,null=True)
    def __str__(self):
          return f'{self.name} - {self.age}'
