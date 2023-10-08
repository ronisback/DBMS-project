from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Invest
from django.contrib.auth.decorators import login_required
from .forms import investform

# Create your views here.

@login_required(login_url='register')
def investview(request):
    form = investform()
    if request.method == 'POST':
        form = investform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invest')
    tmp = Invest.objects.all()
    investments=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            investments.append(
                {'institute':i.institute,
            'description':i.description,
            'amount':i.amount,
            'date':i.date,
            'id':i.id})
    
    context = {
        'form': form,
        'investments': investments,

    }
    return render(request, 'investpage/invest.html', context)
def iidelete(request, id):
    dele = Invest.objects.get(id=id)
    dele.delete()
    return redirect('invest')
def iiupdate(request, id):
    invest = Invest.objects.get(id=id)
    form = investform(instance = invest)
    if request.method == 'POST':
        form = investform(request.POST, instance =invest)
        if form.is_valid():
            form.save()
        return redirect('invest')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)

    

