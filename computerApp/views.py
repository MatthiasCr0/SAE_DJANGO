from django.shortcuts import render
from computerApp.models import Machine, Utilisateur

from django.shortcuts import get_object_or_404, redirect, render
from .forms import  AddMachineForm, AddUtilisateurForm, DelMachineForm, DelUtilisateurForm, DelContactMessageForm, ContactForm
from .models import ContactMessage
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


#@login_required

def index(request) :
    context = {}
    return render(request, 'index.html', context)


def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines':machines}
    return render(request,
        'machine_list.html',
        context)



def machine_detail_view(request, pk) :
    machine = get_object_or_404 (Machine, id=pk)
    context={'machine':machine}
    return render(request,
        'machine_detail.html',
        context)


def machine_add_form(request):
    if request.method == 'POST':
        form_2 = AddMachineForm(request.POST or None)
        if form_2.is_valid():
            new_machine = Machine(
                            nom=form_2.cleaned_data['nom'],
                            ip=form_2.cleaned_data['ip'])
            new_machine.save()
        return redirect('machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request,'machine_add.html',context)


def utilisateur_list_view(request) :
    utilisateurs = Utilisateur.objects.all()
    context={'utilisateurs':utilisateurs}
    return render(request,
        'utilisateur_list.html',
        context)



def utilisateur_detail_view(request, pf) :
    utilisateur = get_object_or_404 (Utilisateur, id=pf)
    context={'utilisateur':utilisateur}
    return render(request,
        'utilisateur_detail.html',
        context)


def utilisateur_add_form(request):
    if request.method == 'POST':
        form_2= AddUtilisateurForm(request.POST or None)
        if form_2.is_valid():
            new_utilisateur = Utilisateur(
                                prenom=form_2.cleaned_data['prenom'],
                                nom=form_2.cleaned_data['nom'],
                                secteur=form_2.cleaned_data['secteur'])
            new_utilisateur.save()
        return redirect('utilisateurs')
    else:
        form = AddUtilisateurForm()
        context = {'form': form}
        return render(request,'utilisateur_add.html',context)



def machine_del_form(request):
    if request.method == 'POST':
        form=DelMachineForm(request.POST or None)
        if form.is_valid():
            selected_machine = form.cleaned_data['selected_machine']
            Machine.objects.filter(pk__in=selected_machine).delete()
        return redirect('machines')

    

def utilisateur_del_form(request):
    if request.method == 'POST':
        form=DelUtilisateurForm(request.POST or None)
        if form.is_valid():
            selected_utilisateur = form.cleaned_data['selected_utilisateur']
            Utilisateur.objects.filter(pk__in=selected_utilisateur).delete()
        return redirect('utilisateurs')


def visualisation_view(request) :
    machines = Machine.objects.all()
    utilisateurs = Utilisateur.objects.all()
    context={'machines':machines,'utilisateurs':utilisateurs}
    return render(request,
        'visualisation.html',
        context)


def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            contact = ContactMessage(name=name, email=email, message=message)
            contact.save()

            return redirect('contact-success')

    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def contact_success(request):
    return render(request, 'contact_success.html')


def contact_messages(request):
    messages = ContactMessage.objects.all()
    return render(request, 'contact_messages.html', {'messages': messages})


def del_contact_message(request):
    if request.method == 'POST':
        form=DelContactMessageForm(request.POST or None)
        if form.is_valid():
            selected_contact_message = form.cleaned_data['selected_contact_message']
            ContactMessage.objects.filter(pk__in=selected_contact_message).delete()
        return redirect('view-contact-messages')
    


