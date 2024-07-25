from django.db import models

# Create your models here.


class payment_model (models.Model):
    p_voucher_number = models.CharField( max_length=50 , null=True)
    p_bankacc = models.CharField( max_length=50 , null=True)
    p_voucher_date = models.DateField( auto_now=False, auto_now_add=False , null=True)
    p_amount_top = models.CharField( max_length=50 , null=True)
    p_voucher_miti = models.CharField( max_length=50 , null=True)
    p_drcr = models.CharField( max_length=50 , null=True)
    p_remarks = models.CharField( max_length=50 , null=True)
    p_particular = models.CharField( max_length=50 , null=True)
    p_total = models.CharField( max_length=50 , null=True)
    p_collected_by = models.CharField( max_length=50 , null=True)

  

class bank_payment_model (models.Model):
    b_p_voucher_number = models.CharField( max_length=50)
    b_p_ledger_name = models.CharField( max_length=50)
    b_p_voucher_date = models.CharField( max_length=50)
    b_p_voucher_miti = models.CharField( max_length=50)
    b_p_toprow_amount = models.CharField( max_length=50)
    b_p_collectedby = models.CharField( max_length=50)
    b_p_drcr = models.CharField( max_length=50)
    b_p_remarks = models.CharField( max_length=50)
    b_p_particular = models.CharField( max_length=50)
    b_table_drcr = models.CharField( max_length=50)
    b_p_table_amount = models.CharField( max_length=50)
    b_p_cheque_no = models.CharField( max_length=50)


