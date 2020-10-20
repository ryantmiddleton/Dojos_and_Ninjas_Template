from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),	
    path('add_dojo', views.addDojo),
    path('add_ninja', views.addNinja),
    path('delete_dojo/<int:dojo_id_to_del>', views.deleteDojo),
]