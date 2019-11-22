from django.db import models

# Create your models here.

class PartyName(models.Model):
    name = models.CharField(max_length=10,verbose_name='姓名')
    telephone = models.CharField(max_length=11,verbose_name='手机号码')

    def __str__(self):
        #return  self.name
         return  self


