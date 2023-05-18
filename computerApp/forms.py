from django import forms
from .models import Machine
from .models import Utilisateur
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form) :
    nom = forms.CharField(required=True, label="Nom de la machine")
    def clean_id(self):
        data = self.cleaned_data["nom"]
        if len(data) >20 :
            raise ValidationError("Erreur de format pour le champ nom")
        return data

    

class AddUtilisateurForm(forms.Form) :

    nom = forms.CharField(required=True, label="Nom de l'utilisateur")
    prenom = forms.CharField(required=True, label="Prenom de l'utilisateur")

    def clean_prenom(self):
        data = self.cleaned_data["prenom"]
        if len(data) >20:
            raise ValidationError("Erreur de format pour le champ prenom")
        return data

    def clean_nom (self):
        data = self.cleaned_data["nom"]
        if len(data) >20:
            raise ValidationError("Erreur de format pour le champ nom")
        return data


class DelMachineForm(forms.Form):
    selected_machine = forms.ModelMultipleChoiceField(
        queryset=Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )


class DelUtilisateurForm(forms.Form):
    selected_utilisateur = forms.ModelMultipleChoiceField(
        queryset=Utilisateur.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
