from django.contrib import admin
from paymentapp.models import payment_model , bank_payment_model

# Register your models here.
admin.site.register(payment_model)
admin.site.register(bank_payment_model)