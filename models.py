from django.db import models

# Create your models here.




#########################
#main
#########################
class typeWrite(models.Model):

    title = models.CharField(max_length=100)
    text = models.CharField(max_length=200)
    textStyle = models.ForeignKey('txtStyle')

    pause = models.IntegerField(default=0)

    def __str__(self):
        return self.title



#########################
#Subs
#########################

#########################
#txtStyle
#########################

class txtStyle(models.Model):

    title = models.CharField(max_length=100)
    color = models.CharField(max_length=6)
    family = models.CharField(max_length=20)
    bkgColor = models.CharField(max_length=6)
    size =  models.CharField(max_length=6 )


    def __str__(self):
        return self.title

