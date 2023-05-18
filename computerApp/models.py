from django.db import models
from datetime import datetime

# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('switch', ('Switch - To maintains and connect servers')),
    )
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length = 20, default='NomParDefault')
    maintenanceDate = models.DateField(default = datetime.now())
    match= models.CharField(max_length = 32, choices=TYPE, default='PC')



class Utilisateur(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length = 20)
    prenom = models.CharField(max_length = 20)
    


    #def __str__(self):
    #   return str(self.id) + " -> " + self.nom + " " + self.nom
    #
    #def get_name(self):
    #   return str(self.id) + " " + self.nom + " " + self.nom
