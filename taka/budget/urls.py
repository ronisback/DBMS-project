from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.budgetview, name='budget'),
    path('delete/<int:id>',views.bdelete, name='delete'),
    path('update/<int:id>',views.bupdate, name='update'),

   
    
]
