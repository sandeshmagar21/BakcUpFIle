from django.shortcuts import render, redirect
from .models import Gym
from .forms import GymCreate
from django.http import HttpResponse

def index(request):
    records = Gym.objects.all()
    return render(request, 'GYMApp/Premium.htm', {'records': records})
def upload(request):
    upload = GymCreate()
    if request.method == 'POST':
        upload = GymCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'GYMApp/Upload_form.htm', {'Upload_form':upload})
def update_Gym(request, Gym_id):
    Gym_id = int(Gym_id)
    try:
        Gym_sel = Gym.objects.get(id = Gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    Gym_form = GymCreate(request.POST or None, instance = Gym_sel)
    if Gym_form.is_valid():
       Gym_form.save()
       return redirect('index')
    return render(request, 'GYMApp/Upload_form.htm', {'Upload_form':Gym_form})
def delete_Gym(request, Gym_id):
    Gym_id = int(Gym_id)
    try:
        Gym_sel = Gym.objects.get(id = Gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    Gym_sel.delete()
    return redirect('index')