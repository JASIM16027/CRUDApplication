from django.shortcuts import render
from .forms import StudentAddForm
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.

def add_show(request):
    if request.method=='POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            form = StudentAddForm()

    else:
        form = StudentAddForm()
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html',context={'form':form,'student':stud})


#this function will update / edit
def update_show(request,update_id):
    if request.method=="POST":
        upd = User.objects.get(pk=update_id)
        form = StudentAddForm(request.POST,instance=upd)
        if form.is_valid():
            form.save()
    

    else:
        upd = User.objects.get(pk=update_id)
        form = StudentAddForm(instance=upd)

    return render(request,'enroll/updatestudent.html',{'form':form})




# this function will delete data
def delete_data(request,id):
    if request.method=='POST':
        dlt = User.objects.get(pk=id)
        dlt.delete()
    return HttpResponseRedirect('/')