from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializers,EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(empcompany=company)
            emps_serializer=EmployeeSerializers(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            return Response({'error_msg':'Company might not exist!!'})


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializers