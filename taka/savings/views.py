from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Savings
from django.contrib.auth.decorators import login_required
from .forms import savingsform

# Create your views here.

@login_required(login_url='register')
def saveview(request):
    form = savingsform()
    if request.method == 'POST':
        form = savingsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('savings')
    tmp = Savings.objects.all()
    savings=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            savings.append(
                {'amount':i.amount,
            'description':i.description,
            'date':i.date,
            'id':i.id})
    
    context = {
        'form': form,
        'savings': savings,

    }
    return render(request, 'savingspage/save.html', context)
def sdelete(request, id):
    dele = Savings.objects.get(id=id)
    dele.delete()
    return redirect('savings')
def supdate(request, id):
    savings = Savings.objects.get(id=id)
    form = savingsform(instance = savings)
    if request.method == 'POST':
        form = savingsform(request.POST, instance =savings)
        if form.is_valid():
            form.save()
        return redirect('savings')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)

    

