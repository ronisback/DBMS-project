from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Debt
from django.contrib.auth.decorators import login_required
from .forms import debtform

# Create your views here.

@login_required(login_url='register')
def debtview(request):
    form = debtform()
    if request.method == 'POST':
        form = debtform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('debt')
    tmp = Debt.objects.all()
    debts=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            debts.append(
                {'debtor':i.debtor,
            'description':i.description,
            'amount':i.amount,
            'date':i.date,
            'id':i.id})
    
    context = {
        'form': form,
        'debts': debts,

    }
    return render(request, 'debtpage/debtp.html', context)
def ddelete(request, id):
    dele = Debt.objects.get(id=id)
    dele.delete()
    return redirect('debt')
def dupdate(request, id):
    debt = Debt.objects.get(id=id)
    form = debtform(instance = debt)
    if request.method == 'POST':
        form = debtform(request.POST, instance =debt)
        if form.is_valid():
            form.save()
        return redirect('debt')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)
    

