from django.shortcuts import render
from computerApp.models import Machine
from computerApp.models import Utilisateur
from django.shortcuts import get_object_or_404, redirect
from .forms import  AddMachineForm
from .forms import AddUtilisateurForm

#@login_required
# Create your views here.
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
        form_1 = AddMachineForm(request.POST or None)
        if form_1.is_valid():
            new_machine = Machine(nom=form_1.cleaned_data['nom'])
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
                                id=form_2.cleaned_data['id'],
                                nom=form_2.cleaned_data['nom'])
            new_utilisateur.save()
            return redirect('utilisateurs')
    else:
        form = AddUtilisateurForm()
        context = {'form': form}
        return render(request,'utilisateur_add.html',context)




