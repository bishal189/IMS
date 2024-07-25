from django import forms
from .models import Company

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'name',
            'address',
            'email',
            'contact_no',
            'country',
            'province',
            'pan_no',
            'company_type',
            'mobile_no',
            'financial_year',
        ]
