from django.db import models
import uuid

# Create your models here.
class Book(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="generated unique id for book")
    name=models.CharField(max_length=100,help_text='Book Name',null=True)
    purchase_date=models.DateField(null=True,blank=True)
    Publication=models.ManyToManyField('Publication',help_text='Publication of book')
    book_author=models.ForeignKey('Author', on_delete=models.SET_NULL,help_text='Book Author',null=True)
    purchase_date=models.DateField(null=True,blank=True)
    timestamp=models.DateField(auto_now=True)
  
def __str__(self):
    return self.name 

class Author(models.Model):
    id=models.AutoField(primary_key=True)
    author_name=models.CharField(max_length=100,help_text='Author Name',null=True)
    numChoice=(
        ('1','One'),
        ('2','two'),
        ('3','Three'),
        ('4','Four'),
        ('5','five'),
    )
    total_book_written=models.CharField(max_length=1,choices=numChoice,null=True)
    date_of_birth=models.DateField('Birth',null=True,blank=True)
    date_of_death=models.DateField('Death',null=True,blank=True)
    timestamp=models.DateField(auto_now=True)
   
def __str__(self):
    return self.name 

class Publication(models.Model):
    name=models.CharField(max_length=100,help_text='Book Publication Name')
    Address=models.CharField(max_length=100,help_text='Publication address',null=True)

def __str__(self):
    return self.name +' - '+self.Address