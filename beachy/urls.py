from django.urls import path
from . import views



# Create you views here
urlpatterns = [
    path('index/',views.index, name="home"),
   
]

