from django.shortcuts import render, redirect
from starbucks.forms import MainMenuForm
from starbucks.forms import updateMenuForm
from starbucks.forms import statusMenuForm
from starbucks.models import MainMenu

# Create your views here.

def index(request):
    listmenu = MainMenu.objects.all()
    return render(request, 'index.html', {'listmenu' : listmenu})
def add(request):
    if request.method == "POST":
        form = MainMenuForm(request.POST)
        if form.is_valid():
            try:
                # for testing in console
                # print("aaa")
                form.save()
                return redirect('/menu')
            except:
                pass
    else:
        form = MainMenuForm()
    return render(request, 'form.html', {'form' : form})
def delete(request, id):
    target = MainMenu.objects.get(id = id)
    target.delete()
    return redirect('/menu')
def edit(request, id):
    target = MainMenu.objects.get(id = id)
    return render(request, 'form.html', {'form' : target})
def editPost(request, id):
    target = MainMenu.objects.get(id = id)
    # let say we want to update specific fields only, we can use another model 
    # in this case i only allow the qty n name update only so i use the updateMenuForm model
    form = updateMenuForm(request.POST, instance = target)
    if form.is_valid():  
        form.save()  
        return redirect("/menu")  
    return render(request, 'edit.html', {'form': target})  
def updateStatus(request, id):
    target = MainMenu.objects.get(id = id)
    if target.status == 0:
        target.status = 1
    else:
        target.status = 0
    target.save()
    return redirect("/menu")