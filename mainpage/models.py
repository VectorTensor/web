from django.db import models

# Create your models here.
def get_image_path_comment(instance, filename):
    return os.path.join('mainpage\media\photos\comment', str(instance.id), filename)

def get_image_path_Question(instance, filename):
    return os.path.join('mainpage\media\photos\Question', str(instance.id), filename)


def get_image_path_Answer(instance, filename):
    return os.path.join('mainpage\media\photos\Answer', str(instance.id), filename)






class Answer(models.Model):
    About= models.CharField(max_length=200)
    Image=models.ImageField(upload_to=get_image_path_Answer,blank=True,null=True)
    thumbsup=models.IntegerField(max_length=64)




class Question(models.Model):
    About=models.CharField(max_length=200)
    Image= models.ImageField(upload_to=get_image_path_Question,blank=True,null=True)
    Primary_answer=models.ForeignKey(Answer,on_delete=models.CASCADE)
    
class comment(models.Model):
    About = models.CharField(max_length=200)
    Image= models.ImageField(upload_to=get_image_path_comment,blank=True,null=True)
    Question= models.ForeignKey(Question,on_delete=models.CASCADE)
