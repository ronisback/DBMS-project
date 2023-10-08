from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.incomeview, name="income"),
    path('delete/<int:id>',views.idelete, name='idelete'),
    path('iupdate/<int:id>',views.iupdate, name='iupdate'),
    
]
