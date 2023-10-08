from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.investview, name="invest"),
    path('iidelete/<int:id>',views.iidelete, name='iidelete'),
    path('iiupdate/<int:id>',views.iiupdate, name='iiupdate'),
    
]
