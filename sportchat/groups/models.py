from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    group_description = models.TextField()
    members = models.ManyToManyField('Member', related_name='groups')

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=255)
    # You can add more fields for the member if needed

    def __str__(self):
        return self.name


# Create your models here.

