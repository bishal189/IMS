from django.shortcuts import render,redirect
from company.forms import CompanyForm
from .models import Company
from .utils import sanitize_db_name
from django.core.management import call_command
from django.conf import settings
from django.shortcuts import get_object_or_404, render
from .models import Company
from django.db import connections,OperationalError
import os
from .utils import get_db_path,create_company_database

def company_home(request):
    company=Company.objects.all()
    context={
        'companies':company
    }
    return render(request,'landing.html',context)



def company_landing(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    sanitized_name = sanitize_db_name(company.name)
    print(f"Sanitized name: {sanitized_name}")

    # Create a mapping from sanitized company names to database aliases
    database_alias=sanitized_name
    connection_message = ""
    
    try:
        # Ensure the connection is established
        connection = connections[database_alias]
        connection.ensure_connection()
        
        connection_message = f"Successfully connected to the database '{database_alias}'."
        print(connection_message)  # Output to console for debugging

        # Example query to test the connection (optional)
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM  masterapp_customer ")  # Replace with your actual query
            results = cursor.fetchall()
            print(results)
        
        return render(request, 'menu.html', {
            'company': company,
            'connection_message': connection_message,
            # 'results': results
        })
    
    except OperationalError as e:
        connection_message = f"Error connecting to database '{database_alias}': {e}"
        print(connection_message)  # Output to console for debugging
        return render(request, 'menu.html', {
            'company': company,
            'connection_message': connection_message,
            
        })

    
def create_company(request):
    if request.method=='POST':
        
        form = CompanyForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('company_home')
        
    else:
        
        return redirect('company_home')
        
        
        
    
