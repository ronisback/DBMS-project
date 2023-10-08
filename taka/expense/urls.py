from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.expenseview, name="expense"),
    path('delete/<int:id>',views.edelete, name='edelete'),
    path('dupdate/<int:id>',views.eupdate, name='eupdate'),
    
]
