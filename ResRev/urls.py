from django.urls import path
from . import views

app_name='ResRev'
urlpatterns = [
    path('', views.home, name='home'),
    
]
    # {% for name in latest_animal_name %}
    #     <li><a href="/animalSite/{{ Animal.id }}/">{{ name.animal_name }}</a></li>
    # {% endfor %}
