from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from users_app.forms import CustomForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request,("New User Account Created!"))
        return redirect('register')
    else:

        form = CustomForm()
        return render(request, 'register.html',{'register_form':form})

