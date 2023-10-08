from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Account
from django.contrib.auth.decorators import login_required
from .forms import accountsform

# Create your views here.

@login_required(login_url='register')
def accountview(request):
    form = accountsform()
    if request.method == 'POST':
        form = accountsform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts')
    tmp = Account.objects.all()
    accounts=[]
    for i in tmp:
        if str(i.owner)==request.session['user']:
            accounts.append(
                {'type':i.type,
                 'name':i.name,
            'description':i.description,
            'id':i.id})
    
    context = {
        'form': form,
        'accounts': accounts,

    }
    return render(request, 'accountpage/account.html', context)
def adelete(request, id):
    dele = Account.objects.get(id=id)
    dele.delete()
    return redirect('accounts')
def aupdate(request, id):
    account = Account.objects.get(id=id)
    form = accountsform(instance = account)
    if request.method == 'POST':
        form = accountsform(request.POST, instance =account)
        if form.is_valid():
            form.save()
        return redirect('accounts')

    context = {'form': form}
    return render(request, 'budgetpage/update.html', context)

    

