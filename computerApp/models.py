from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows')),
        ('Mac', ('Mac - Run MacOS')),
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('switch', ('Switch - To maintains and connect servers')),
    )

    VLAN = (
        ('Gestion',('77')),
        ('Clients',('10')),
        ('Services',('20')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length = 20, default='NomParDefault')
    maintenanceDate = models.DateTimeField(auto_now_add=True)
    mach = models.CharField(max_length = 32, choices=TYPE, default='PC')
    ip = models.CharField(max_length = 32, default='127.0.0.1')
    vlan = models.CharField(max_length= 32, choices=VLAN, default='Aucun')
    maj = models.CharField(max_length= 32, default='Jamais modifié')
    user = models.CharField(max_length= 32, default='Aucun')

    def __str__(self):
        return self.nom

    def save(self, *args, **kwargs):
        self.maintenanceDate = timezone.now() 
        super().save(*args, **kwargs)



class Utilisateur(models.Model):

    SECT = (
        ('Gestion',('77')),
        ('Clients',('10')),
        ('Services',('20')),
    )


    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length = 20)
    prenom = models.CharField(max_length = 20)
    secteur = models.CharField(max_length= 32, choices=SECT, default='Gestion')
    


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name