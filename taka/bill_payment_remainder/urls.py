from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.billview, name="payment"),
    path('bbdelete/<int:id>',views.bbdelete, name='bbdelete'),
    path('bbupdate/<int:id>',views.bbupdate, name='bbupdate'),
    
]
