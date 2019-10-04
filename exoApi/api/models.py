from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categories(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    statut = models.BooleanField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class SousCategories(models.Model):
    categorie=models.ForeignKey(Categories,on_delete=models.CASCADE,related_name='categorie')
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    statut = models.BooleanField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Articles(models.Model):
    sousCategorie=models.ForeignKey(SousCategories,on_delete=models.CASCADE,related_name='souscategorie')
    nom = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    statut = models.BooleanField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now_add=True)
        
    def __str__(self):
        return self.name

class Commentaires(models.Model):
    article=models.ForeignKey(SousCategories,on_delete=models.CASCADE,related_name='article')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    description = models.TextField()
    statut = models.BooleanField()
    date_add=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now_add=True)