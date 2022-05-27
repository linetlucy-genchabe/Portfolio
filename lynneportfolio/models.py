from django.db import models
import datetime as dt

# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['first_name']


class Project(models.Model):
    title = models.CharField(max_length =60)
    description = models.TextField()
    editor = models.ForeignKey(Editor,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)
    project_image = models.ImageField(upload_to = 'project/',blank=True)

class Skills(models.Model):
    name= models.CharField(max_length =60)

class Certifications(models.Model):
    name= models.CharField(max_length =60)
    certifications_image = models.ImageField(upload_to = 'certifications/',blank=True)

   
