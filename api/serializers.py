from rest_framework import serializers
from api.models import *

#Company Serializer
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    company_id=serializers.ReadOnlyField()
    class Meta:
        model=Company
        fields="__all__"

#Employee Serializer
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    empid=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"