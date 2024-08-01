from django.shortcuts import render
from . forms import contactForm,StudentData,PasswordValidationProject
# Create your views here.

def Django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./formapp/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
    
    else:
        form=contactForm()
    return render(request, './home/home.html',{'form':form})

def Studentform(request):
    if request.method=='POST':
        form = StudentData(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
       form = StudentData()
    return render(request, './home/home.html',{'form':form})


def PasswordValidation(request):
    if request.method=='POST':
        form = PasswordValidationProject(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordValidationProject()
    return render(request, './home/home.html',{'form':form})