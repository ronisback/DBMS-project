from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Income
from django.contrib.auth.decorators import login_required
from .forms import incomeform

# Create your views here.

@login_required(login_url='register')
def incomeview(request):
    form = incomeform()
    if request.method == 'POST':
        form = incomeform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('income')
    tmp = Income.objects.all()
    incomes=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            incomes.append(
                {'category':i.category,
            'description':i.description,
            'amount':i.amount,
            'date':i.date,
            'id':i.id})
    
    context = {
        'form': form,
        'incomes': incomes,

    }
    return render(request, 'incomepage/incomep.html', context)
def idelete(request, id):
    dele = Income.objects.get(id=id)
    dele.delete()
    return redirect('income')
def iupdate(request, id):
    income = Income.objects.get(id=id)
    form = incomeform(instance = income)
    if request.method == 'POST':
        form = incomeform(request.POST, instance =income)
        if form.is_valid():
            form.save()
        return redirect('income')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)

    

