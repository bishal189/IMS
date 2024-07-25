from django.contrib import admin
from salesapp.models import sales_inv_data,VoucherTracker,DealerSetup,ProductModel
# Register your models here.

admin.site.register(sales_inv_data)
admin.site.register(VoucherTracker)
admin.site.register(DealerSetup)
admin.site.register(ProductModel)
