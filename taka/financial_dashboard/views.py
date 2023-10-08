from django.shortcuts import render
from income.models import Income
from expense.models import Expense
from debt.models import Debt
from investment.models import Invest
from savings.models import Savings

# Create your views here.

def financial(request):
    tmp = Income.objects.all()
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    for i in tmp:
        if str(i.owner)==request.session['user']:
            sum1 += i.amount

    tmp2 = Expense.objects.all()
    for i in tmp2:
        if str(i.owner) == request.session['user']:
            sum2 += i.amount

    tmp3 = Debt.objects.all()
    for i in tmp3:
        if str(i.owner) == request.session['user']:
            sum3 += i.amount

    tmp4 = Invest.objects.all()
    for i in tmp4:
        if str(i.owner) == request.session['user']:
            sum4 += i.amount

    tmp5 = Savings.objects.all()
    for i in tmp5:
        if str(i.owner) == request.session['user']:
            sum5 += i.amount

    current_balance = sum1-sum2+sum3-sum4-sum5
    context = {
        'sum1':sum1,
        'sum2':sum2,
        'sum3':sum3,
        'sum4':sum4,
        'sum5':sum5,
        'current_balance':current_balance
    }
    return render(request, 'Financialdash/finance.html',context)