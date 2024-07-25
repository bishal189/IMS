from django.contrib import admin

# Register your models here.
from .models import Company


class CompanyRegister(admin.ModelAdmin):
    list_display=['name','company_type','address','country','financial_year']
admin.site.register(Company,CompanyRegister)