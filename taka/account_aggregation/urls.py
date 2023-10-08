from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.accountview, name="accounts"),
    path('adelete/<int:id>',views.adelete, name='adelete'),
    path('aupdate/<int:id>',views.aupdate, name='aupdate'),
    
]
