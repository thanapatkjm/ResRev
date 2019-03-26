from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def home(request):
    return render(request, 'home.html')
    # return render(request, 'table.html', {'animal_field':animal_field,"animal_list":animal_list})
