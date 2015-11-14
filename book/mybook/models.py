# coding:utf-8
from django.db import models

# Create your models here.
class Author(models.Model):
    AuthorID = models.AutoField(primary_key = True)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Country = models.CharField(max_length=70)
    
class Book(models.Model):
    ISBN = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    AuthorID = models.ForeignKey(Author)
    Publisher = models.CharField(max_length=100)
    PublishDate = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)


    