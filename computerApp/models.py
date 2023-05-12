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
    id = models.CharField(primary_key=True, editable=False, max_length = 4)
    nom = models.CharField(max_length = 6, default='None')
    #maintenanceDate = models.DateField(default = datetime.now())
    #match= models.CharField(max_length = 32,choices=TYPE,default='PC')



class Utilisateur(models.Model):
    id = models.CharField(primary_key=True, editable=True, max_length = 4)
    nom = models.CharField(max_length = 10)
    prenom = models.CharField(max_length = 10)
    
#    def __str__(self):
#        return str(self.id) + " -> " + self.nom + " " + self.prenom
#
#    def get_name(self):
#        return str(self.id) + " " + self.nom + " " + self.prenom


