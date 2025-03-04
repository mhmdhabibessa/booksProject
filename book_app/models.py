from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=45)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # books  = [book,book,book]
class Book(models.Model):
    title = models.CharField(max_length=45)
    description= models.TextField()
    img= models.TextField()
    author = models.ForeignKey(Author,related_name="books",on_delete=models.CASCADE,null=True)
    is_published = models.BooleanField()
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# publishers 

class Publisher(models.Model):
    name = models.CharField(max_length=45)
    books = models.ManyToManyField(Book,related_name="publishers")
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    rate = models.IntegerField(max=5,min=0,default=4)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
