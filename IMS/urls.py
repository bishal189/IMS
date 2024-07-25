from django.contrib import admin
from django.urls import path,include
from IMS import views
from IMS .views import login_page

from salesapp import views as sales_views
from receiptapp import views as receipt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_page, name='login_page'),
    path('',include('company.urls')),
    path('menu_page/', views.menu_page, name='menu_page'),
    path('customer_setup/', views.customer_setup, name='customer_setup'), 
    path('suplier_setup/', views.suplier_setup, name='suplier_setup'), 
    path('supplier/<int:id>/',views.partial,name='partial'),
    path('edit_supplier/<int:id>/',views.edit_supplier_view,name='edit_supplier'),
    path('delete_supplier/<int:id>/',views.delete_supplier,name='delete_supplier'),
    path('create/supplier/',views.create_supplier,name='create_supplier'),
    path('i_setup/', views.i_setup, name='i_setup'), 
    path('ledger_set/', views.ledger_set, name='ledger_set'), 
    path('create_user/', views.create_user, name='create_user'), 
    path('unit_setup/', views.unit_setup, name='unit_setup'), 
    path('user_maintain/', views.user_maintain, name='user_maintain'),
    path('sales_invoice/', views.sales_invoice, name='sales_invoice'),
    path('salesconfig/', views.salesconfig, name='salesconfig'),
    path('journal_voucher/', views.journal_voucher, name='journal_voucher'),
    path('purchase_invoice/', views.purchase_invoice, name='purchase_invoice'),
    path('cash_receipt/', views.cash_receipt, name='cash_receipt'),
    path('payment/', views.payment, name='payment'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('create_notes/', views.create_notes, name='create_notes'),
    path('settings/', views.settings, name='settings'),
    path('sales_reports/', views.sales_reports, name='sales_reports'),
    path('purchase_reports/', views.purchase_reports, name='purchase_reports'),
    path('cash_payments_reports/', views.cash_payments_reports, name='cash_payments_reports'),
    path('receipt_reports/', views.receipt_reports, name='receipt_reports'),
    path('task_list/', views.task_list, name='task_list'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('create_group/', views.create_group, name='create_group'),
    path('customer_report/', views.customer_report, name='customer_report'),
    path('item_report/', views.item_report, name='item_report'),
    path('ledger_report/', views.ledger_report, name='ledger_report'),
    path('error_page/', views.error_page, name='error_page'),
    path('log_out/', views.log_out, name='log_out'),
    path('login_error/', views.login_error, name='login_error'),
    path('tersms_condition/', views.tersms_condition, name='tersms_condition'),
    path('customer_category/', views.customer_category, name='customer_category'),
    path('create_supplier/', views.create_supplier, name='create_supplier'),
    path('create_s_group/', views.create_s_group, name='create_s_group'),
    path('create_s_terms/', views.create_s_terms, name='create_s_terms'),
    path('inner_supplier/', views.inner_supplier, name='inner_supplier'),
    path('create_s_category/', views.create_s_category, name='create_s_category'),
    path('create_s_report/', views.create_s_report, name='create_s_report'),
    path('main_item_nav/', views.main_item_nav, name='main_item_nav'),
    path('dealer_setup/', views.dealer_setup, name='dealer_setup'),

    path('sales_bank_receipt/', receipt_views.sales_bank_receipt, name='sales_bank_receipt'),
    path('sales_cash_receipt/', receipt_views.sales_cash_receipt, name='sales_cash_receipt'),
    path('report_home/', views.report_home, name='report_home'),


    # path('main_item_nav1/', views.main_item_nav1, name=''),
    path('inner_data/', views.inner_data, name='inner_data'),
    path('item_group/', views.item_group, name='item_group'),
    path('bank_receipt/', views.bank_receipt, name='bank_receipt'),
    path('bank_payment/', views.bank_payment, name='bank_payment'),
    path('bank_payment_report/', views.bank_payment_report, name='bank_payment_report'),
    path('payment_edit/<int:id>', views.payment_edit, name='payment_edit'),
    path('bank_payment_edit/<int:id>', views.bank_payment_edit, name='bank_payment_edit'),
    
  #edit urls
    path('edit/item_setup/<int:id>/',views.edit_main_nav_item,name='edit_item'),
    path('delete/item_setup/<int:id>/',views.Delete_item,name='delete_item'),

    path('customer_data_ajax/',views.customer_data_ajax, name='customer_data_ajax'),
    
    #Create Voucher
    path('create_voucher/',sales_views.create_voucher,name='create_voucher'),

    #get product detail ajax
    path('get_product_detail_ajax',views.get_product_detail_ajax,name="get_product_detail_ajax"),

    #get dealer name for party in sales
    path('get_dealer_for_party',views.get_dealer_for_party,name='get_dealer_for_party'),
    
    
    # daybook
    
    path('day_book',views.Day_book,name='day_book')


]

