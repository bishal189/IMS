from django.contrib import admin
from .models import CashReceipt,BankReceipt
# Register your models here.
admin.site.register(CashReceipt)
admin.site.register(BankReceipt)
