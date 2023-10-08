from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.debtview, name="debt"),
    path('ddelete/<int:id>',views.ddelete, name='ddelete'),
    path('dupdate/<int:id>',views.dupdate, name='dupdate'),
    
    
]
