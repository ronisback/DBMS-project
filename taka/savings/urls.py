from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.saveview, name="savings"),
    path('sdelete/<int:id>',views.sdelete, name='sdelete'),
    path('supdate/<int:id>',views.supdate, name='supdate'),
    
]
