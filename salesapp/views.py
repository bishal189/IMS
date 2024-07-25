
import json

from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse

from .models import VoucherTracker


def create_voucher(request):
    try:
        if not request.user.is_authenticated:
            raise Exception("You should be logged in to perform this action")
        data=request.POST
        print(data)
        suffix=data.get('Sufix')
        prefix=data.get('Prefix')
        body_length=data.get('body_length')
        voucher_type=data.get('voucher_type')

        voucher,created=VoucherTracker.objects.get_or_create(user=request.user,voucher_type=voucher_type)
        voucher.prefix=prefix
        voucher.suffix=suffix
        voucher.voucher_length=body_length
        voucher.save()
            

        if voucher_type=="sales_invoice":
            return redirect(reverse('sales_invoice'))
        elif voucher_type=="purchase_invoice":
            return redirect(reverse('purchase_invoice'))

        return render(request,'Setups/salesconfog.html',{
            'message':"Configuration created successfully"
        })



    except Exception as e:
        return render(request,'Setups/salesconfog.html',{
            'error':f"Unexpected error {str(e)}"
        })

