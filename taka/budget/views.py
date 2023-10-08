from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Budgets
from django.contrib.auth.decorators import login_required
from .forms import budgetform

# Create your views here.

@login_required(login_url='register')
def budgetview(request):
    form = budgetform()
    if request.method == 'POST':
        form = budgetform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('budget')
    tmp = Budgets.objects.all()
    budgets=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            budgets.append(
                {'category':i.category,
            'description':i.description,
            'spendings':i.spendings,
            'date':i.date,
            'id':i.id})
    
    context = {
        'form': form,
        'budgets': budgets,

    }
    return render(request, 'budgetpage/budgetp.html', context)
def bdelete(request, id):
    dele = Budgets.objects.get(id=id)
    dele.delete()
    return redirect('budget')

def bupdate(request, id):
    budget = Budgets.objects.get(id=id)
    form = budgetform(instance = budget)
    if request.method == 'POST':
        form = budgetform(request.POST, instance =budget)
        if form.is_valid():
            form.save()
        return redirect('budget')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)   

