from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Bill
from django.contrib.auth.decorators import login_required
from .forms import billform

# Create your views here.

@login_required(login_url='register')
def billview(request):
    form = billform()
    if request.method == 'POST':
        form = billform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
    tmp = Bill.objects.all()
    payments=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            payments.append(
                {'bill_name':i.bill_name,
                 'payee':i.payee,
                 'account_number':i.account_number,
            'description':i.description,
            'amount':i.amount,
            'due_date':i.due_date,
            'status':i.status,
            'id':i.id})
    
    context = {
        'form': form,
        'payments': payments,

    }
    return render(request, 'billpage/bill.html', context)
def bbdelete(request, id):
    dele = Bill.objects.get(id=id)
    dele.delete()
    return redirect('payment')
def bbupdate(request, id):
    bill = Bill.objects.get(id=id)
    form = billform(instance = bill)
    if request.method == 'POST':
        form = billform(request.POST, instance =bill)
        if form.is_valid():
            form.save()
        return redirect('payment')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)
    

