
from . import views
from django.urls import path
urlpatterns = [
    path('create_company/',views.company_home,name='company_home'),
    path('company/<int:company_id>/',views.company_landing,name='company_landing'),
    path('create/company/',views.create_company,name='create_company'),
]