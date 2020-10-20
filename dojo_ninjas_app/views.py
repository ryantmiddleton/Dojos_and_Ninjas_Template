from django.shortcuts import render, redirect
from dojo_ninjas_app.models import dojos, ninjas

# Create your views here.
def index(request):
    context = {
        'Dojos': dojos.objects.all()
    }
    return render(request, "index.html", context)
    
def addDojo(request):
    dojos.objects.create(
        name = request.POST['dojo_name'],
        city = request.POST['dojo_city'],
        state = request.POST['dojo_state']
    )
    return redirect("/")

def addNinja(request):
    ninjas.objects.create(
        first_name = request.POST['first_name_txt'],
        last_name = request.POST['last_name_txt'],
        dojo_id = dojos.objects.get(id=request.POST['dojo_sel'])
    )
    return redirect("/")

def deleteDojo(request, dojo_id_to_del):
    dojos.objects.get(id=dojo_id_to_del).delete()
    for ninja in ninjas.objects.filter(dojo_id=dojo_id_to_del):
        ninja.delete()
    return redirect("/")