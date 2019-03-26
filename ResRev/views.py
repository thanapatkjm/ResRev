from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

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


# <form action="{% url 'animal:created' %}" method="get">
#   <input type="submit" value="Sign In">
# </form>
