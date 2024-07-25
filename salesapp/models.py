from django.db import models
# from django.contrib.auth.models import User

from masterapp.models import item_setup, ledger_setup
from userauth.models import User

from masterapp.models import Customer, customer_group_model
# Create your models here.
class ProductModel(models.Model):


    product=models.ForeignKey(item_setup,on_delete=models.CASCADE,blank=True,null=True)

    qty=models.FloatField()
    price=models.FloatField()
    discount=models.CharField(max_length=10)
    vat=models.CharField(max_length=10)
    total=models.FloatField()

class sales_inv_data (models.Model):
    voucher_number = models.CharField( max_length=50 , null=True)
    customer_name = models.CharField( max_length=50 , null=True)
    refrence_number = models.CharField( max_length=50 , null=True)
    voucher_date = models.DateField(auto_now=False, auto_now_add=False ,null=True)
    voucher_miti = models.CharField(max_length=50 , null=True)
    paymenth_method = models.CharField(max_length=50 , null=True)
    remarks = models.CharField(max_length=50 , null=True)
    discount = models.CharField(max_length=50 , null=True)
    sub_total = models.CharField(max_length=50 , null=True)
    vat = models.CharField( max_length=50)
    grand_total = models.CharField( max_length=50)
    product = models.ManyToManyField(ProductModel)
    status=models.CharField(max_length=20,default='pending')
    created_at=models.DateField(auto_now_add=True)
    
 


class VoucherTracker(models.Model):
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    prefix=models.CharField(max_length=100,null=True)
    suffix=models.CharField(max_length=100,null=True)
    voucher_length=models.IntegerField(null=True)
    counter=models.IntegerField(default=1,null=True)
    voucher_type=models.CharField(max_length=50)
    status=models.CharField(max_length=20,default='pending')


class DealerSetup(models.Model):
    dealer_name=models.CharField(max_length=100)
    group=models.ForeignKey(customer_group_model,on_delete=models.CASCADE)
    customers=models.ManyToManyField(Customer)
