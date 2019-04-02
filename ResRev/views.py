from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

import uuid
import hashlib
import base64
import bcrypt

def home(request):
    return render(request, 'home.html')
    # return render(request, 'table.html', {'animal_field':animal_field,"animal_list":animal_list})

def new_rest(request):
    pass

def register(request):
    pass

def rest_page(request):
    pass

def reviewer(request):
    pass

def registering(request):
    if(request.POST['password']==request.POST['Cpassword']):
        password=request.POST['password']
        salt = uuid.uuid4().hex
        hashed = hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
        return HttpResponseRedirect(reverse('ResRev:home'))
    else:
        err = "Password is not corrected"
        return render(request, 'Register.html',{"err" : err },)

# <form action="{% url 'animal:created' %}" method="get">
#   <input type="submit" value="Sign In">
# </form>
