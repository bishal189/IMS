from django.db import models

# Create your models here.
class Customer(models.Model):
    profile = models.ImageField( upload_to=None, height_field=None, width_field=None, max_length=None , null=True)
    under_parrent  = models.CharField( max_length=50 , null=True)
    email  = models.CharField( max_length=50 , null=True)
    agent_id  = models.CharField( max_length=50 , null=True)
    branch_name  = models.CharField( max_length=50 , null=True)
    aria_name  = models.CharField( max_length=50 , null=True)
    representive  = models.CharField( max_length=50 , null=True)
    supervisor  = models.CharField( max_length=50 , null=True)
    group = models.CharField(max_length=255)
    terms = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    name = models.CharField(max_length=255 , blank=True)
    address = models.TextField()
    pan = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    linkid = models.CharField(max_length=255)
    customer_type = models.CharField(max_length=255)
    account_no = models.CharField(max_length=255)




class item_setup(models.Model):
    iteam_image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None  , null=True)
    select_group = models.CharField( max_length=50  , null=True)
    unit_choice = models.CharField( max_length=50  , null=True)
    alt_unit = models.CharField( max_length=50  , null=True)
    item_name = models.CharField( max_length=50  , null=True)
    barcode = models.CharField( max_length=50  , null=True)
    item_code = models.CharField( max_length=50  , null=True)
    hs_code = models.CharField( max_length=50  , null=True)
    cost_price = models.CharField( max_length=50  , null=True)
    sales_rate = models.CharField( max_length=50  , null=True)
    enable_non_tax = models.BooleanField(("")   , null=True)

    def __str__(self):
        return self.item_name +  self.item_code



class ledger_setup(models.Model):
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100, blank=True, null=True)
    nature = models.CharField(max_length=100)
    account_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    cheque_no = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name



class unit_model (models.Model):
    unit_name = models.CharField( max_length=50)
    unit_symbol = models.CharField( max_length=50)
    unit_extra = models.CharField( max_length=50)



class user_model (models.Model):
    userroles = models.CharField( max_length=50)
    username = models.CharField( max_length=50)
    password = models.CharField( max_length=50)
    allowWebAccess = models.CharField( max_length=50)



class item_group_model (models.Model):
    item_under_group = models.CharField( max_length=50)
    groupid = models.CharField( max_length=50)
    item_group_name = models.CharField( max_length=50)
    item_nature = models.CharField( max_length=50)
    undergroup=models.CharField(default='primary',null=True,blank=True,max_length=100)
    group_name=models.CharField(max_length=100,null=True,blank=True)
    
    
    def __str__(self):
        return self.item_group_name
    


class customer_group_model(models.Model):
    customer_under_group = models.CharField(max_length=50 , null = True , blank=True)
    customer_group_id = models.CharField(max_length=50)    
    customer_group_name = models.CharField(max_length=50)
    customer_account_id = models.CharField(max_length=50)
    customer_parrent = models.CharField(max_length=50 , null = True , blank=True)
    

#defined by the bishal for supplier

class SupplierGroup(models.Model):
    supplier_under_group = models.CharField(max_length=50 , null = True , blank=True)
    supplier_group_id = models.CharField(max_length=50,null=True,blank=True)    
    supplier_group_name = models.CharField(max_length=50,null=True,blank=True)
    supplier_account_id = models.CharField(max_length=50,null=True,blank=True)
    supplier_parrent = models.CharField(max_length=50 , null = True , blank=True)
    

    
    

    def __str__(self):
        return self.supplier_group_name  



class Supplier(models.Model):
    profile=models.ImageField(null=True,blank=True)
    group=models.CharField(max_length=50,null=True,blank=True)
    terms_condition = models.TextField(blank=True,null=True)
    supplier_category = models.CharField(max_length=255, blank=True,null=True)
    supplier_type = models.CharField(max_length=255, blank=True,null=True)
    under_parent = models.CharField(max_length=255, blank=True,null=True)
    name = models.CharField(max_length=255, blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    pan = models.CharField(max_length=255, blank=True,null=True)
    account_number = models.CharField(max_length=255, blank=True,null=True)
    phone_number = models.CharField(max_length=255, blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    link_account_id = models.CharField(max_length=255, blank=True,null=True)
    link_agent_id = models.CharField(max_length=255, blank=True,null=True) 
    branch_name = models.CharField(max_length=255, blank=True,null=True)
    aria_name = models.CharField(max_length=255, blank=True,null=True) 
    representative = models.CharField(max_length=255, blank=True,null=True)
    supervisor = models.CharField(max_length=255, blank=True,null=True)
    
    
    def __str__(self):
        return self.name 
  

