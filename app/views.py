from django.shortcuts import render
from app.form import customerform
from django.http import HttpResponse
def sample(request):
    form= customerform
    if request.method=='POST':
     form=customerform(request.POST)
     if form.is_valid():
        form.save()
        return HttpResponse('inserted')
    return render(request,'home.html',{'form':form})

