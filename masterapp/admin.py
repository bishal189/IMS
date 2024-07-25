# admin.py in your app
from django.contrib import admin
from .models import Customer, item_setup, ledger_setup  , unit_model ,user_model , item_group_model , customer_group_model
from django.contrib import admin
from .models import Supplier,SupplierGroup
 # Import all three models

class ItemSetupAdmin(admin.ModelAdmin):
    pass  # Add any specific configuration for the item_setup model admin if needed

# Register the models with their respective admin configurations
admin.site.register(Customer)
admin.site.register(item_setup, ItemSetupAdmin)
admin.site.register(ledger_setup)
admin.site.register(unit_model)
admin.site.register(user_model)
admin.site.register(item_group_model)
admin.site.register(customer_group_model)


from django.contrib import admin
from .models import Supplier



admin.site.register(SupplierGroup)

admin.site.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
