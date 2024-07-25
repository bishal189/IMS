from django.http import JsonResponse
from django.shortcuts import render,redirect,reverse
from django.views.decorators.csrf import csrf_exempt
from masterapp.models import ledger_setup
import json
# Create your views here.
@csrf_exempt
def sales_bank_receipt(request):
    if request.method=='POST':
        data=json.loads(request.body)
        request.session['sales_bank_amount']=data.get('amount')
        request.session['sales_bank_ledger']=data.get('ledger')
        return JsonResponse({'status':'ok'},status=200)



@csrf_exempt
def sales_cash_receipt(request):
    if request.method=='POST':
        data=json.loads(request.body)
        amount=data.get('amount')
        request.session['sales_cash_amount']=amount
        return JsonResponse({'status':'ok'},status=200)



