from django.contrib import admin
from .models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_id','companyname','companylocation','companyabout','companyabout','companyadded_date','companystatus')
    search_fields=('companyname',)

admin.site.register(Company,CompanyAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('empid','empname','empemail','empaddress','empphone','empposition','empcompany')
    list_filter=('empposition',)

admin.site.register(Employee,EmployeeAdmin)