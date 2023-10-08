from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Expense
from django.contrib.auth.decorators import login_required
from .forms import expenseform

# Create your views here.

@login_required(login_url='register')
def expenseview(request):
    form = expenseform()
    if request.method == 'POST':
        form = expenseform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense')
    
    if request.user.is_authenticated:
        user_id = request.user.id  # Assuming the user's ID is stored in the session
    
    
    tmp = Expense.objects.all()
    expenses=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            expenses.append(
                {'category':i.category,
            'description':i.description,
            'amount':i.amount,
            'date':i.date,
            'id':i.id})
    

 
    context = {
        'form': form,
        'expenses': expenses,
    }
    return render(request, 'expensepage/expensep.html', context)
def edelete(request, id):
    dele = Expense.objects.get(id=id)
    dele.delete()
    return redirect('expense')
def eupdate(request, id):
    expense = Expense.objects.get(id=id)
    form = expenseform(instance = expense)
    if request.method == 'POST':
        form = expenseform(request.POST, instance =expense)
        if form.is_valid():
            form.save()
        return redirect('expense')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)

    

