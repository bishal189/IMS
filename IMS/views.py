import random
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User  # Import the User model
from django.http import JsonResponse
from masterapp.models import Supplier,SupplierGroup
from django.urls import reverse
from crm.models import Todo
from masterapp.models import Customer
from masterapp.models import item_setup
from masterapp.models import ledger_setup
from masterapp.models import unit_model
from receiptapp.models import BankReceipt, CashReceipt
from salesapp.models import DealerSetup, ProductModel, sales_inv_data,VoucherTracker
from masterapp.models import user_model
from paymentapp.models import payment_model, bank_payment_model
from masterapp.models import item_group_model
from masterapp.models import customer_group_model
from django.shortcuts import get_object_or_404,redirect

from userauth.models import User


@login_required(login_url="/")
def menu_page(request):
    users = User.objects.all()  # Get all users
    return render(request, 'menu.html', {'users': users})


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Authenticate user
        user = authenticate(request, email=email, password=password)
        print(user,'user is printd here')
        if user is not None:
            # Login the user
            login(request, user)
            # Redirect to the Menu Page on successful login
            return HttpResponseRedirect(reverse('company_home'))
        else:
            # Redirect to the login error page on authentication failure
            return HttpResponseRedirect(reverse('login_error'))
    if request.user.is_authenticated:
        return redirect("company_home")
    return render(request, 'index.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")


def login_error(request):
    return render(request, "Errors/loginerror.html")


#! This Is To Create Customer Area
# Redirect to the login page if not authenticated

def customer_data_ajax(request):
    parent_group_filter = request.GET.get("group", None)
    print(parent_group_filter,'parent_group_filter')
    name=request.GET.get('name',None)
    if parent_group_filter:
        n_customer_parrent = customer_group_model.objects.filter(
            customer_parrent=parent_group_filter).values_list('customer_group_name', flat=True)
        n_customer_parrent = list(n_customer_parrent)
        n_customer_parrent.append(parent_group_filter)
        real_cus_data = Customer.objects.filter(group__in=n_customer_parrent)
        real_cus_data = Customer.objects.filter(group=parent_group_filter)

    elif name:
        real_cus_data=Customer.objects.filter(name=name).first()
        data={

            'name':real_cus_data.name,
            'group':real_cus_data.group,
            'email':real_cus_data.email,
            'pan':real_cus_data.pan,
            'phone':real_cus_data.phone,
            'address':real_cus_data.address,
        }
        return JsonResponse({'data':data})
    else:
        real_cus_data = Customer.objects.all()

    context = {}
    context['customers'] = real_cus_data
    return render(request, "Setups/customer_ajax_data.html", context)

def inner_data(request):
    group_name = request.GET.get('group', None)
 
    if group_name:
        item_data = item_setup.objects.filter(select_group=group_name)
    else:
        item_data = item_setup.objects.all()
    item_groups = item_group_model.objects.all()
    print('i am inner display')
        
   
    context={
            'item_data':item_data,
            'item_group':item_groups,
        }
    return render(request,'ItemSetup/inner.html',context)



@login_required(login_url="/")
def customer_setup(request):
    new_group = customer_group_model.objects.all()

    parent_group_filter = request.GET.get("group", None)

    customer_parents = customer_group_model.objects.filter(
        customer_parrent=None).values()

    childs = customer_group_model.objects.exclude(
        customer_parrent=None).order_by('id').values()

    if parent_group_filter:
        # n_customer_parrent = customer_group_model.objects.filter(
        #   customer_parrent=parent_group_filter).values_list('customer_group_name', flat=True)

        # n_customer_parrent = list(n_customer_parrent)
        # n_customer_parrent.append(parent_group_filter)

        real_cus_data = Customer.objects.filter(group=parent_group_filter)
        # real_cus_data = Customer.objects.filter(group__in=n_customer_parrent)

    else:
        real_cus_data = Customer.objects.all()

    return render(request, "Setups/customer.html", {'customer_childs': list(childs), 'customer_parents': customer_parents, 'new_group': new_group, 'real_cus_data': real_cus_data})


@login_required(login_url="/")
def create_customer(request):
    if request.method == 'GET':
        customer_group_database = customer_group_model.objects.all()

        context = {
            'customer_group_database': customer_group_database
        }
        return render(request, "CustomerSetup/createcustomer.html", context)
    else:
        profile = request.POST.get('profile')
        under_parrent = request.POST.get('under_parrent')
        email = request.POST.get('email')
        agent_id = request.POST.get('agent_id')
        branch_name = request.POST.get('branch_name')
        aria_name = request.POST.get('aria_name')
        representive = request.POST.get('representive')
        supervisor = request.POST.get('supervisor')
        group = request.POST.get('group')
        terms = request.POST.get('terms')
        category = request.POST.get('category')
        name = request.POST.get('name')
        address = request.POST.get('address')
        pan = request.POST.get('pan')
        phone = request.POST.get('phone')
        linkid = request.POST.get('linkid')
        customer_type = request.POST.get('customer_type')
        account_no = request.POST.get('account_no')

        new_customer = Customer(
            profile=profile,
            under_parrent=under_parrent,
            email=email,
            agent_id=agent_id,
            branch_name=branch_name,
            aria_name=aria_name,
            representive=representive,
            supervisor=supervisor,
            group=group,
            terms=terms,
            category=category,
            name=name,
            address=address,
            pan=pan,
            phone=phone,
            linkid=linkid,
            customer_type=customer_type,
            account_no=account_no
        )
        new_customer.save()

        return HttpResponseRedirect('/customer_setup')


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def customer_report(request):
    customer_data = Customer.objects.all()
    return render(request, "CustomerSetup/CustomerReport.html", {'customer_data': customer_data})


def tersms_condition(request):
    return render(request, "CustomerSetup/termsandcondition.html")


def customer_category(request):
    return render(request, "CustomerSetup/category.html")


@login_required(login_url="/")
def create_group(request):
    if request.method == 'POST':
        
        customer_under_group = request.POST.get('customer_under_group')
        customer_group_id = request.POST.get('customer_group_id')
        customer_group_name = request.POST.get('customer_group_name')
        customer_account_id = request.POST.get('customer_account_id')
        customer_parent = request.POST.get('customer_parrent')
        # parent_group = request.POST.get('parent_group')/

        if customer_parent == 'None':
            customer_parent = None

        if customer_group_name:
            # Create a new group
            customer_database = customer_group_model(
                customer_under_group=customer_under_group,
                customer_group_id=customer_group_id,
                customer_group_name=customer_group_name,
                customer_account_id=customer_account_id,
                customer_parrent=customer_parent,
            )
        else:
            # Create a new subgroup
            parent_group = get_object_or_404(
                customer_group_model, customer_group_name=customer_parent)
            customer_database = customer_group_model(
                customer_under_group=customer_under_group,
                customer_group_id=customer_group_id,
                customer_account_id=customer_account_id,
                customer_parrent=customer_parent,

            )

        customer_database.save()

        return HttpResponseRedirect(reverse('customer_setup'))

    else:
        group_group = customer_group_model.objects.all()

        context = {
            'group_group': group_group
        }

        return render(request, "CustomerSetup/creategroup.html", context)


#! For Suppliers Creation
# Redirect to the login page if not authenticated

#

def partial(request,id):
    if id:
        group_data =SupplierGroup.objects.get(id=id)
        all_data=Supplier.objects.filter(group=group_data)
        
   
    data={
        'item_data':all_data,
        
    }
  
    return render(request,'SupplierSetup/inner.html',data)

def supplier1_setup(request):
    return render(request,"Setups/suppliers.html")



def delete_supplier(request,id):
    try:
        supplier=Supplier.objects.get(id=id)
        supplier.delete()
        return redirect('suplier_setup')
    
    except:
        pass
        

#here 
def create_s_terms(request):
    return render(request, "SupplierSetup/terms.html")


def create_s_category(request):
    
    return render(request, "SupplierSetup/category.html")


def create_s_report(request):
    supplier=Supplier.objects.all()
    print(supplier,'data of supplier')
    context={
        'supplier':supplier
    }
    return render(request, "SupplierSetup/sreport.html",context)


#! For Create item Setup

# Redirect to the login page if not authenticated
@login_required(login_url="/")
def i_setup(request):
    if request.method == 'GET':
        i_udata = unit_model.objects.all()
        i_group_data = item_group_model.objects.all()

        context = {
            'i_udata': i_udata,
            'i_group_data': i_group_data
        }
        return render(request, "ItemSetup/item.html", context)
    else:
        iteam_image = request.POST.get('iteam_image')
        select_group = request.POST.get('select_group')
        unit_choice = request.POST.get('unit_choice')
        alt_unit = request.POST.get('alt_unit')
        item_name = request.POST.get('item_name')
        barcode = request.POST.get('barcode')
        item_code = request.POST.get('item_code')
        hs_code = request.POST.get('hs_code')
        cost_price = request.POST.get('cost_price')
        sales_rate = request.POST.get('sales_rate')
        enable_non_tax = request.POST.get('enable_non_tax')

        # Convert string value to boolean for enable_non_tax
        enable_non_tax = request.POST.get('enable_non_tax') == 'on'

        iteam_model = item_setup(
            iteam_image=iteam_image,
            select_group=select_group,
            unit_choice=unit_choice,
            alt_unit=alt_unit,
            item_name=item_name,
            barcode=barcode,
            item_code=item_code,
            hs_code=hs_code,
            cost_price=cost_price,
            sales_rate=sales_rate,
            enable_non_tax=enable_non_tax
        )
        iteam_model.save()

    return HttpResponseRedirect(reverse('item_report'))



@login_required(login_url="/")
def main_item_nav(request):
    group = request.GET.get('group', None)
  
    if group:
        item_data = item_setup.objects.filter(select_group=group)
    else:
        item_data = item_setup.objects.all()
    item_groups = item_group_model.objects.filter(item_under_group='Primary')
    secondary_group = item_group_model.objects.filter( item_under_group='Secondary')
    
    context = {
        'item_data': item_data,
        'item_group': item_groups,
        'secondary_group':secondary_group
    }
    return render(request, 'ItemSetup/itemnav.html', context)

    



# Redirect to the login page if not authenticated
@login_required(login_url="/")
def item_group(request):
    if request.method == 'GET':
        return render(request, "ItemSetup/itemgroup.html")

    else:
        item_under_group = request.POST.get('item_under_group')
        groupid = request.POST.get('groupid')
        item_group_name = request.POST.get('item_group_name')
        item_nature = request.POST.get('item_nature')
      
        item_database_model = item_group_model(
            item_under_group=item_under_group,
            groupid=groupid,
            item_group_name=item_group_name,
            item_nature=item_nature,
        )

        item_database_model.save()

        return HttpResponseRedirect(reverse('i_setup'))


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def item_report(request):
    show_data = item_setup.objects.all()
    return render(request, "ItemSetup/itemrepot.html", {'show_data': show_data})


#! for Create Ledger
# Redirect to the login page if not authenticated
    
@login_required(login_url="/")
def ledger_set(request):
    if request.method == 'POST':
        ledger_name = request.POST.get('ledger_name')
        alias = request.POST.get('alias')
        ledger_nature = request.POST.get('ledger_nature')
        
        # Initialize the ledger object with common fields
        ledger = ledger_setup(
            name=ledger_name,
            alias=alias,
            nature=ledger_nature
        )
        
        # If the ledger name contains 'bank', add bank-specific fields
        if 'bank' in ledger_name.lower():
            ledger.account_name = request.POST.get('account_name')
            ledger.account_number = request.POST.get('account_number')
            ledger.branch = request.POST.get('branch')
            ledger.cheque_no = request.POST.get('cheque_no')
        
        ledger.save()
        
        return redirect('ledger_report')  # Redirect to a success page
    
    return render(request, 'Setups/ledger.html')



# Redirect to the login page if not authenticated
@login_required(login_url="/")
def ledger_report(request):
    ledg_data = ledger_setup.objects.all()
    return render(request, "Reports/ledgerreport.html", {'ledg_data': ledg_data})


@login_required(login_url="/")
def create_user(request):
    if request.method == 'GET':
        return render(request, "Setups/createuser.html")

    elif request.method == 'POST':
        userroles = request.POST.get('userroles')
        username = request.POST.get('username')
        password = request.POST.get('password')
        allowWebAccess = request.POST.get('allowWebAccess')

        # Check if the user with the given username already exists
        if User.objects.filter(username=username).exists():
            error_message = "Username already exists. Please choose a different username."
            return render(request, "Setups/createuser.html", {'error_message': error_message})

        # Create user
        user_data = User.objects.create_user(
            username=username,
            password=password,
        )

        # Authenticate and login the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("/user_maintain")
        else:
            # Handle authentication failure (optional)
            error_message = "Invalid username or password. Please try again."
            return render(request, "Setups/createuser.html", {'error_message': error_message})


#! For create Useracess
@login_required(login_url="/")
def user_maintain(request):
    users = User.objects.all()
    return render(request, "Setups/useracess.html", {'users': users})


#! For Create Unit
# Redirect to the login page if not authenticated
@login_required(login_url="/")
def unit_setup(request):
    if request.method == 'GET':
        return render(request, "ItemSetup/unit.html")

    else:
        unit_name = request.POST.get('unit_name')
        unit_symbol = request.POST.get('unit_symbol')
        unit_extra = request.POST.get('unit_extra')

        model = unit_model(
            unit_name=unit_name,
            unit_symbol=unit_symbol,
            unit_extra=unit_extra
        )

        model.save()
        return HttpResponseRedirect('/unit_setup')


# ** Entry Section

# Redirect to the login page if not authenticated

@login_required(login_url="/")
def sales_invoice(request):
    if request.method == 'GET':
        idata = item_setup.objects.all()
        cdata = Customer.objects.all()
        ldata = ledger_setup.objects.all()
        udata = unit_model.objects.all()
        ledger_data = ledger_setup.objects.all()

        voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="sales_invoice").first()
        if voucher is not None:
            voucher_no=f'{voucher.suffix}/{0:0{voucher.voucher_length}}{voucher.counter}/{voucher.prefix}'
        else:
            voucher_no=""

        context = {
            'cdata': cdata,
            'idata': idata,
            'ldata': ldata,
            'ledger_data':ledger_data,
            'udata': udata,
            'voucher_no':voucher_no,
            'voucher':voucher,
        }

        return render(request, "Entry/salesinvoice.html", context)
    else:
        print(request.POST)
        voucher_number = request.POST.get('voucher_number')
        customer_name = request.POST.get('customer_name')
        refrence_number = request.POST.get('refrence_number')
        voucher_miti = request.POST.get('voucher_miti')
        voucher_date=request.POST.get('voucher_date')
        paymenth_method = request.POST.get('paymenth_method')
        remarks = request.POST.get('remarks')
        vat = request.POST.get('vat')
        grand_total = request.POST.get('grand_total')
        discount=request.POST.get('discount[]')
        sub_total=request.POST.get('sub_total')

        product = request.POST.getlist('product')
        product_qty=request.POST.getlist('qty[]')
        product_vat=request.POST.getlist('vat[]')
        product_price=request.POST.getlist('price[]')
        product_discount=request.POST.getlist('discount[]')
        product_total=request.POST.getlist('total[]')




        sales_data = sales_inv_data.objects.create(
            voucher_number=voucher_number,
            customer_name=customer_name,
            refrence_number=refrence_number,  # Corrected spelling here
            voucher_miti=voucher_miti,
            paymenth_method = paymenth_method,
            remarks=remarks,
            discount=discount,
            sub_total=sub_total,
            vat=vat,
            grand_total=grand_total,
            voucher_date=voucher_date
        )
        sales_cash_amount=request.session.pop('sales_cash_amount',None)
        sales_bank_amount=request.session.pop('sales_bank_amount',None)
        total_payment=0


        if sales_cash_amount is not None:
            voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="cash_receipt").first()
            voucher_no=""
            if voucher is not None:
                voucher_no=f'{voucher.prefix}/{0:0{voucher.voucher_length}}{voucher.counter}'
                voucher.counter+=1
                voucher.save()
            else:
                voucherTrackerInstance=VoucherTracker.objects.create(user=request.user,voucher_type='cash_receipt',prefix='cr',voucher_length=4)
                voucher_no=f'cr/{0:0{voucherTrackerInstance.voucher_length}}1'

            total_payment+=int(sales_cash_amount)
            cash_receipt=CashReceipt.objects.create(voucher_no=voucher_no,reference_no=voucher_number,voucher_date=voucher_date,voucher_miti=voucher_miti,remarks=remarks,amount=int(sales_cash_amount))
            
        if sales_bank_amount is not None:
            voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="bank_receipt").first()
            voucher_no=''
            if voucher is not None:
                voucher_no=f'{voucher.prefix}/{0:0{voucher.voucher_length}}{voucher.counter}'
                voucher.counter+=1
                voucher.save()
            else:
                voucherTrackerInstance=VoucherTracker.objects.create(user=request.user,voucher_type='bank_receipt',prefix='br',voucher_length=4)
                voucher_no=f'br/{0:0{voucherTrackerInstance.voucher_length}}1'


            sales_bank_ledger=request.session.pop('sales_bank_ledger') 
            ledger=ledger_setup.objects.filter(name=sales_bank_ledger).first()
            bank_receipt=BankReceipt.objects.create(voucher_no=voucher_no,reference_no=voucher_number,voucher_date=voucher_date,voucher_miti=voucher_miti,remarks=remarks,amount=int(sales_bank_amount),ledger=ledger)
            total_payment+=int(sales_bank_amount)

        print(total_payment)

        if total_payment>=int(grand_total):
            sales_data.status='paid'

        for i in range(0,len(product)):
            item_setup_instance=item_setup.objects.filter(item_name=product[i]).first()
            if item_setup_instance is None:
                item_setup_instance=None

            else:
                product_instance=ProductModel.objects.create(product=item_setup_instance,qty=product_qty[i],
                                                         vat=product_vat[i],price=product_price[i],total=product_total[i],discount=product_discount[i])
                sales_data.product.add(product_instance)


        sales_data.save()
        
        voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="sales_invoice").first()
        if voucher is not None:
            voucher.counter+=1
            if voucher.status=='pending':
                voucher.status='activated'
            voucher.save()
        return HttpResponseRedirect("/sales_reports")



def salesconfig(request):
    voucher_type = request.GET.get('type', '')  # Retrieve the 'type' query parameter value
    return render(request, 'Setups/salesconfog.html',{'voucher_type':voucher_type})


# journal voucher


def journal_voucher(request):
    j_bank_ledger = ledger_setup.objects.all()
    context = {
        'j_data': j_bank_ledger
    }
    return render(request, "Entry/journal.html", context)


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def purchase_invoice(request):
    try:
        idata = item_setup.objects.all()
        sdata = Supplier.objects.all()
        ldata = ledger_setup.objects.all()
        udata = unit_model.objects.all()

        voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="purchase_invoice").first()
        if voucher is not None:
            voucher_no=f'{voucher.suffix}/{0:0{voucher.voucher_length}}{voucher.counter}/{voucher.prefix}'
        else:
            voucher_no=""

        context = {
            'sdata': sdata,
            'idata': idata,
            'ldata': ldata,
            'udata': udata,
            'voucher_no':voucher_no
        }
        print(context)

        return render(request, "Entry/purchaseinvoice.html",context)
    except Exception as e:
        return render(request,"Entry/purchaseinvoice.html",{'error':f"Unexpected error {str(e)}"})


# Redirect to the login page if not authenticated
@login_required(login_url="/")
#! this is ued for cash receipt
def cash_receipt(request):
    if request.method=='GET':
        voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="cash_receipt").first()
        voucher_no=''
        if voucher is not None:
            voucher_no=f'{voucher.prefix}/{0:0{voucher.voucher_length}}{voucher.counter}'
        else:
            voucherTrackerInstance=VoucherTracker.objects.create(user=request.user,voucher_type='cash_receipt',prefix='cr',voucher_length=4)
            voucher_no=f'cr/{0:0{voucherTrackerInstance.voucher_length}}1'
        context={
            'voucher_no':voucher_no
        }
        return render(request, "Entry/receipt.html", context)
    elif request.method=='POST':
            print(request.POST)
            data=request.POST
            voucher_no=data.get('p_voucher_number')
            reference_no=data.get('reference_no','101010')
            voucher_date=data.get('p_voucher_date')
            voucher_miti=data.get('p_voucher_miti')
            amount=data.get('p_total')
            remarks=data.get('p_remarks')
        
            voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="cash_receipt").first()
            voucher.counter+=1
            voucher.save()

            cash_receipt=CashReceipt.objects.create(voucher_no=voucher_no,reference_no=reference_no,voucher_date=voucher_date,voucher_miti=voucher_miti,remarks=remarks,amount=amount)
            return redirect(reverse('cash_receipt'))




def bank_receipt(request):
    if request.method=='GET':
        ledgers = ledger_setup.objects.all()

        voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="bank_receipt").first()
        voucher_no=''
        if voucher is not None:
            voucher_no=f'{voucher.prefix}/{0:0{voucher.voucher_length}}{voucher.counter}'
        else:
            voucherTrackerInstance=VoucherTracker.objects.create(user=request.user,voucher_type='bank_receipt',prefix='br',voucher_length=4)
            voucher_no=f'br/{0:0{voucherTrackerInstance.voucher_length}}1'

        context={
            'ledgers':ledgers,
            'voucher_no':voucher_no
        }
        return render(request, "Entry/bankreceipt.html",context)
    elif request.method=="POST":
            print(request.POST)
            data=request.POST
            voucher_no=data.get('b_p_voucher_number')
            reference_no=data.get('reference_no')
            voucher_date=data.get('b_p_voucher_date')
            voucher_miti=data.get('b_p_voucher_miti')
            amount=data.get('b_p_table_amount')
            ledger_name=data.get('b_r_ledger_name')
            ledger=ledger_setup.objects.filter(name=ledger_name).first()
            remarks=data.get('b_p_remarks',"")
        
            voucher=VoucherTracker.objects.filter(user=request.user,voucher_type="bank_receipt").first()
            voucher.counter+=1
            voucher.save()

            bank_receipt=BankReceipt.objects.create(voucher_no=voucher_no,reference_no=reference_no,voucher_date=voucher_date,voucher_miti=voucher_miti,remarks=remarks,amount=amount,ledger=ledger)
            return redirect(reverse('bank_receipt'))



# Redirect to the login page if not authenticated
@login_required(login_url="/")
#! This is Used For Cash Payment
def payment(request):
    if request.method == 'GET':
        leddata = ledger_setup.objects.all()

        context = {
            'leddata': leddata
        }

        return render(request, "Entry/cashpayment.html", context)
    else:
        p_voucher_number = request.POST.get('p_voucher_number')
        p_bankacc = request.POST.get('p_bankacc')
        p_voucher_date = request.POST.get('p_voucher_date')
        p_amount_top = request.POST.get('p_amount_top')
        p_voucher_miti = request.POST.get('p_voucher_miti')
        p_drcr = request.POST.get('p_drcr')
        p_remarks = request.POST.get('p_remarks')
        p_particular = request.POST.get('p_particular')
        p_total = request.POST.get('p_total')
        p_collected_by = request.POST.get('p_collected_by')

    pay_data = payment_model(
        p_voucher_number=p_voucher_number,
        p_bankacc=p_bankacc,
        p_voucher_date=p_voucher_date,
        p_amount_top=p_amount_top,
        p_voucher_miti=p_voucher_miti,
        p_drcr=p_drcr,
        p_remarks=p_remarks,
        p_particular=p_particular,
        p_total=p_total,
        p_collected_by=p_collected_by,

    )

    pay_data.save()
    return HttpResponseRedirect("/cash_payments_reports")


def payment_edit(request, id):
    payment_entry = payment_model.objects.get(id=id)
    leddata = ledger_setup.objects.all()
    context = {
        'edited': payment_entry,
        'leddata': leddata,
    }
    return render(request, "Entry/cashpayment.html", context)


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def cash_payments_reports(request):
    payment_model_data = payment_model.objects.all
    return render(request, "Reports/paymentreport.html", {'payment_model_data': payment_model_data})


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def bank_payment(request):
    bank_ledger = ledger_setup.objects.all()
    context = {
        'bank_ledger': bank_ledger
    }
    if request.method == 'GET':
        return render(request, "Entry/bankpayment.html", context)

    else:
        b_p_voucher_number = request.POST.get('b_p_voucher_number')
        b_p_ledger_name = request.POST.get('b_p_ledger_name')
        b_p_voucher_date = request.POST.get('b_p_voucher_date')
        b_p_voucher_miti = request.POST.get('b_p_voucher_miti')
        b_p_toprow_amount = request.POST.get('b_p_toprow_amount')
        b_p_collectedby = request.POST.get('b_p_collectedby')
        b_p_drcr = request.POST.get('b_p_drcr')
        b_p_remarks = request.POST.get('b_p_remarks')
        b_p_particular = request.POST.get('b_p_particular')
        b_table_drcr = request.POST.get('b_table_drcr')
        b_p_table_amount = request.POST.get('b_p_table_amount')
        b_p_cheque_no = request.POST.get('b_p_cheque_no')

        bank_payment = bank_payment_model(
            b_p_voucher_number=b_p_voucher_number,
            b_p_ledger_name=b_p_ledger_name,
            b_p_voucher_date=b_p_voucher_date,
            b_p_voucher_miti=b_p_voucher_miti,
            b_p_toprow_amount=b_p_toprow_amount,
            b_p_collectedby=b_p_collectedby,
            b_p_drcr=b_p_drcr,
            b_p_remarks=b_p_remarks,
            b_p_particular=b_p_particular,
            b_table_drcr=b_table_drcr,
            b_p_table_amount=b_p_table_amount,
            b_p_cheque_no=b_p_cheque_no,
        )

        bank_payment.save()

        return HttpResponseRedirect("/bank_payment_report")


def bank_payment_report(request):
    bank_model_data = bank_payment_model.objects.all()
    return render(request, "Reports/bankpreport.html", {'bank_model_data': bank_model_data})


def bank_payment_edit(request, id):
    bank_payment_entry = bank_payment_model.objects.get(id=id)
    leddata = ledger_setup.objects.all()
    context = {
        'edited': bank_payment_entry,
        'leddata': leddata,
    }
    return render(request, "Entry/bankpayment.html", context)


# ? CRM Section

# Redirect to the login page if not authenticated
@login_required(login_url="/")
def create_task(request):
    if request.method == 'GET':
        return render(request, "CRM/task.html")

    else:
        part_name = request.POST.get('part_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('adress')
        website = request.POST.get('website')
        designation = request.POST.get('designation')
        task = request.POST.get('task')
        priority = request.POST.get('priority')
        handled_by = request.POST.get('handledby')
        status = request.POST.get('status')

        Database = Todo(
            part_name=part_name,
            contact=contact,
            email=email,
            address=address,
            website=website,
            designation=designation,
            task=task,
            priority=priority,
            handled_by=handled_by,
            status=status
        )
        Database.save()
        return HttpResponseRedirect('/task_list')


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def task_list(request):
    tasks = Todo.objects.all()
    return render(request, "CRM/TaskList.html", {'tasks': tasks})


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def create_contact(request):
    return render(request, "CRM/contact.html")


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def create_notes(request):
    return render(request, "CRM/notes.html")


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def settings(request):
    return render(request, "Setups/settings.html")


# Reports
# Redirect to the login page if not authenticated
@login_required(login_url="/")
def sales_reports(request):
    sales_data = sales_inv_data.objects.all()
    return render(request, "Reports/salesreport.html", {'sales_data': sales_data})


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def purchase_reports(request):
    return render(request, "Reports/purchasereport.html")


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def receipt_reports(request):
    return render(request, "Reports/receiptreport.html")


# Redirect to the login page if not authenticated
@login_required(login_url="/")
def error_page(request):
    return render(request, "Errors/same_error.html")



def edit_main_nav_item(request,id):
    if request.method=='GET':
        item_data=item_setup.objects.get(id=id)
        group_data=item_group_model.objects.all()
        unit_data=unit_model.objects.all()
        print('i am get',item_data.unit_choice)
       
        context={
            
            'item_data':item_data,
            'group_data':group_data,
            'unit_data':unit_data,
        }
        return render(request,'ItemSetup/edit.html',context)
    else:
        item_name=request.POST['item_name']
        alt_unit=request.POST['alt_unit']
        bar_code=request.POST['barcode']
        cost_price=request.POST['cost_price']
        iteam_image=request.POST['iteam_image']
        item_code=request.POST['item_code']
        sales_rate=request.POST['sales_rate']
        hs_code=request.POST['hs_code']
        select_group=request.POST['select_group']
        item_data=item_setup.objects.get(id=id)
        item_data.item_name=item_name
        item_data.select_group=select_group
        item_data.alt_unit=alt_unit
        item_data.barcode=bar_code
        item_data.cost_price=cost_price
        item_data.iteam_image=iteam_image
        item_data.item_code=item_code
        item_data.sales_rate=sales_rate
        item_data.hs_code=hs_code
        item_data.save()
        
        return redirect('edit_item', id=id)
        


def Delete_item(request,id):
    try:
        print('delet functions')
        item=item_setup.objects.get(id=id)
        if item:
            item.delete()
          
        
        else:
            pass 
        return redirect('main_item_nav')  
        
    except:
        pass    



def get_product_detail_ajax(request):
    try:
        name=request.GET.get('name')
        item=item_setup.objects.filter(item_name=name).first()
        print(item)
        data={
            'unit':item.unit_choice
        }
        return JsonResponse({'data':data})
    except Exception as e:
        return JsonResponse({"error":f"Unexpected error {str(e)}"},status=400)






def dealer_setup (request):
    if request.method=='GET':
        cdata = Customer.objects.all()
        gdata=customer_group_model.objects.all()

        context={
            'cdata':cdata,
            'gdata':gdata
        }


        return render (request ,'Setups/dealer.html' ,context)
    else:
        try:
            data=request.POST
            dealer_name=data.get('dealerName',None)
            group_id=data.get('group',None)
            customer_ids=data.getlist('customer',None)
            if dealer_name is None or group_id is None:
                raise Exception ("dealer name and group cannot be none")
            if customer_ids is None:
                raise Exception ("At least  One customer should be Selected")
            group = get_object_or_404(customer_group_model, id=group_id)

            dealer = DealerSetup.objects.create(dealer_name=dealer_name, group=group)
        
        # Associate customers with the dealer
            for customer_id in list(customer_ids):
                customer = get_object_or_404(Customer, id=customer_id)
                dealer.customers.add(customer)
            dealer.save()

            cdata = Customer.objects.all()
            gdata=customer_group_model.objects.all()

            context={
                'cdata':cdata,
                'gdata':gdata,
                'message':"Dealer Setup completed successfully"
                }



            return render(request,'Setups/dealer.html',context)
        
        except Exception as e:
            return render(request,'Setups/dealer.html',{'error':f"Unexpected error occured {str(e)}"})
        

def get_dealer_for_party(request):
    try:
        customer_name=request.GET.get('name',None)
        if customer_name is None:
            raise Exception("customer_name required first")
        
        customer=Customer.objects.filter(name=customer_name).first()
        dealer=DealerSetup.objects.filter(customers=customer).order_by('-id').first()
        data={
            'dealer_name':dealer.dealer_name,
            'dealer_group':dealer.group.id,
            'dealer_id':dealer.id
        }
        return JsonResponse({"data":data},status=200)



    except Exception as e:
        return JsonResponse({'error':f"unexpected error occured {str(e)}"},status=400)





# for group creation of supplier Groups 



@login_required(login_url="/")
def create_s_group(request):
    if request.method == 'POST':
     
        print('i am post request')
        
        supplier_under_group = request.POST.get('customer_under_group')
        supplier_group_id = request.POST.get('customer_group_id')
        supplier_group_name = request.POST.get('customer_group_name')
        supplier_account_id = request.POST.get('customer_account_id')
        supplier_parent = request.POST.get('customer_parrent')
        print(supplier_parent,'supplier parent')
       

        if supplier_parent == 'None':
            supplier_parent = None

        print('i am post request 1')
        if supplier_group_name:
            # Create a new group
           
            supplier_database = SupplierGroup(
                supplier_under_group=supplier_under_group,
                supplier_group_id=supplier_group_id,
                supplier_group_name=supplier_group_name,
                supplier_account_id=supplier_account_id,
                supplier_parrent=supplier_parent,
            )
        else:
            # Create a new subgroup
            parent_group = get_object_or_404(
                SupplierGroup, supplier_group_name=supplier_parent)
            supplier_database = SupplierGroup(
                supplier_under_group=supplier_under_group,
                supplier_group_id=supplier_group_id,
                supplier_account_id=supplier_account_id,
                supplier_parrent=supplier_parent,
            )
        print('i am post request 1')
        supplier_database.save()
        print('up to down')

        return redirect('suplier_setup')

    else:
        group_group = SupplierGroup.objects.all()
        print('i am gt request')

        context = {
            'group_group': group_group
        }

        return render(request, "SupplierSetup/group.html", context)








@login_required(login_url="/")
def suplier_setup(request):
    print('i am supplier showing')
    new_group = SupplierGroup.objects.all()

    parent_group_filter = request.GET.get("group", None)

    customer_parents = SupplierGroup.objects.filter(
        supplier_parrent=None).values()

    childs = SupplierGroup.objects.exclude(
        supplier_parrent=None).order_by('id').values()

    if parent_group_filter:
        # n_customer_parrent = customer_group_model.objects.filter(
        #   customer_parrent=parent_group_filter).values_list('customer_group_name', flat=True)

        # n_customer_parrent = list(n_customer_parrent)
        # n_customer_parrent.append(parent_group_filter)

        real_cus_data = Supplier.objects.filter(supplier_under_group=parent_group_filter)
        # real_cus_data = Customer.objects.filter(group__in=n_customer_parrent)

    else:
        real_cus_data = Supplier.objects.all()
        
    print(childs,'childs')    

    return render(request, "SupplierSetup/index.html", {'customer_childs': list(childs), 'customer_parents': customer_parents, 'new_group': new_group, 'real_cus_data': real_cus_data})



def create_supplier(request):
    if request.method=='POST':
        select_group=request.POST['group']
        profile=request.POST['profile']
        terms_condition=request.POST['terms']
        supplier_category=request.POST['category']
        suppler_type=request.POST['customer_type']
        under_parent=request.POST['under_parrent']
        name=request.POST['name']
        address=request.POST['address']
        pan=request.POST['pan']
        account_number=request.POST['account_no']
        phone_number=request.POST['phone']
        email=request.POST['email']
        link_account_id=request.POST['linkid']
        Link_Agent_Id=request.POST['agent_id']
        branch_name=request.POST['branch_name']
        Aria_Name=request.POST['aria_name']
        Representive=request.POST['representive']
        Supervisor=request.POST['supervisor']
        get_obj=SupplierGroup.objects.get(id=select_group)
        Supplier.objects.create(
        group=get_obj,
        terms_condition=terms_condition,
        supplier_category=supplier_category,
        supplier_type=suppler_type,
        under_parent=under_parent,
        name=name,
        address=address,
        pan=pan,
        account_number=account_number,
        phone_number=phone_number,
        email=email,
        link_account_id=link_account_id,
        link_agent_id=Link_Agent_Id,
        branch_name=branch_name,
        aria_name=Aria_Name,
        representative=Representive,
        supervisor=Supervisor,
        profile=profile,
            
        )
        return redirect('create_supplier')

    else:
        supplier=SupplierGroup.objects.all()
        data={
            'supplier_group':supplier
        }       
 

    return render(request, "SupplierSetup/createsupplier.html",data)




def edit_supplier_view(request,id):
    if request.method=='POST':
        group=request.POST['group']
        supplier_group=SupplierGroup.objects.get(id=group)
        profile=request.POST['profile']
        terms_condition=request.POST['terms']
        supplier_category=request.POST['category']
        suppler_type=request.POST['customer_type']
        under_parent=request.POST['under_parrent']
        name=request.POST['name']
        address=request.POST['address']
        pan=request.POST['pan']
        account_number=request.POST['account_no']
        phone_number=request.POST['phone']
        email=request.POST['email']
        link_account_id=request.POST['linkid']
        Link_Agent_Id=request.POST['agent_id']
        branch_name=request.POST['branch_name']
        Aria_Name=request.POST['aria_name']
        Representive=request.POST['representive']
        Supervisor=request.POST['supervisor']   
        supplier=Supplier.objects.get(id=id)
        supplier.profile=profile
        supplier.group=supplier_group
        supplier.terms_condition=terms_condition
        supplier.supplier_category=supplier_category
        supplier.supplier_type=suppler_type
        supplier.under_parent=under_parent
        supplier.name=name
        supplier.address=address
        supplier.pan=pan
        supplier.account_number=account_number
        supplier.email=email
        supplier.phone_number=phone_number
        supplier.link_account_id=link_account_id
        supplier.link_agent_id=Link_Agent_Id
        supplier.branch_name=branch_name
        supplier.aria_name=Aria_Name
        supplier.representative=Representive
        supplier.supervisor=Supervisor
        
        supplier.save()
        return redirect(reverse('edit_supplier', kwargs={'id': id}))
    
    
    else:
        supplier=Supplier.objects.get(id=id)
        supplier_group=SupplierGroup.objects.all()
       
        data={
            'id':id,
            'supplier':supplier,
            'supplier_group':supplier_group
        }
        return render(request,'SupplierSetup/edit.html',data)
    
    
    
    

def inner_supplier(request):
    parent_group_filter = request.GET.get("group", None)
    print(parent_group_filter,'parent_group_filter')
    name=request.GET.get('name',None)
    if parent_group_filter:
        n_customer_parrent = SupplierGroup.objects.filter(
            supplier_parrent=parent_group_filter).values_list('supplier_group_name', flat=True)
        n_customer_parrent = list(n_customer_parrent)
        n_customer_parrent.append(parent_group_filter)
        real_cus_data = Supplier.objects.filter(group__in=n_customer_parrent)
        real_cus_data = Supplier.objects.filter(group=parent_group_filter)

    elif name:
        real_cus_data=Customer.objects.filter(name=name).first()
        data={

            'name':real_cus_data.name,
            'group':real_cus_data.group,
            'email':real_cus_data.email,
            'pan':real_cus_data.pan,
            'phone':real_cus_data.phone,
            'address':real_cus_data.address,
        }
        return JsonResponse({'data':data})
    else:
        real_cus_data = Customer.objects.all()

    context = {}
    context['customers'] = real_cus_data
    return render(request, "SupplierSetup/inner.html", context)





def Day_book(request):
    sales_data=sales_inv_data.objects.all()
    context={
        'sales_data':sales_data
    }
    return render(request,'Reports/day_book.html',context)



def report_home (request):
    return render (request , "Reports/report.html")
