from django import forms
from .models import Machine
from django.core.exceptions import ValidationError

class AddMachineForm(forms.Form) :
    nom = forms.CharField(required=True, label="Nom de la machine")
    id = forms.CharField(required=True, label="ID de la machine")

    def clean_id(self):
        data = self.cleaned_data["nom"]
        if len(data) <10 :
            raise ValidationError("Erreur de format pour le champ nom")
        return data

    

class AddUtilisateurForm(forms.Form) :

    nom = forms.CharField(required=True, label="Nom de l'utilisateur")
    id = forms.CharField(required=True, label="ID de l'utilisateur")

    def clean_id(self):
        data = self.cleaned_data["id"]
        if len(data) >5:
            raise ValidationError("Erreur de format pour le champ nom")
        return data

    def clean_nom (self):
        data = self.cleaned_data["nom"]
        if len(data) == 0:
            raise ValidationError("Erreur de format pour le champ nom")
        return data


class DelMachineForm(forms.Form):
    selected_machine = forms.ModelMultipleChoiceField(
        queryset=Machine.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
