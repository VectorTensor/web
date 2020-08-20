from django.db import models

# Create your models here.




class Answer(models.Model):
    About= models.CharField(max_length=200)
    Image=models.ImageField(upload_to='Answer',blank=True,null=True)
    thumbsup=models.IntegerField()




class Question(models.Model):
    About=models.CharField(max_length=200)
    Image= models.ImageField(upload_to='Question',blank=True,null=True)
    Primary_answer=models.ForeignKey(Answer,on_delete=models.CASCADE,blank=True,null=True)
    
class comment(models.Model):
    About = models.CharField(max_length=200)
    Image= models.ImageField(upload_to='comment',blank=True,null=True)
    Question= models.ForeignKey(Question,on_delete=models.CASCADE)
