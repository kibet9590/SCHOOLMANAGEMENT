from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.title
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=False)
    experience = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    date_posted = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title