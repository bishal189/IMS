from django.db import models

from masterapp.models import ledger_setup

class CashReceipt(models.Model):
    voucher_no=models.CharField(max_length=30)
    reference_no=models.CharField(max_length=30)
    voucher_date=models.DateField()
    voucher_miti=models.DateField()
    amount=models.IntegerField()
    remarks=models.TextField()
    created_at=models.DateField(auto_now_add=True)

class BankReceipt(models.Model):
    voucher_no=models.CharField(max_length=30)
    reference_no=models.CharField(max_length=30)
    ledger=models.ForeignKey(ledger_setup,on_delete=models.CASCADE)
    voucher_date=models.DateField()
    voucher_miti=models.DateField()
    amount=models.IntegerField()
    remarks=models.TextField()
    created_at=models.DateField(auto_now_add=True)

