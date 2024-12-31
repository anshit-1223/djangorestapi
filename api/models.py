from django.db import models

# Create your models here.

#Creating Company Model
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    companyname=models.CharField(max_length=100)
    companylocation=models.CharField(max_length=50)
    companyabout=models.TextField()
    companytype=models.CharField(max_length=100,choices=(('IT','IT Company'),('Non IT','Non IT Company')))
    companyadded_date=models.DateTimeField(auto_now=True)
    companystatus=models.BooleanField(default=True)

    def __str__(self):
        return self.companyname


#Creating Employee Model

class Employee(models.Model):
    empid=models.AutoField(primary_key=True)
    empname=models.CharField(max_length=100)
    empemail=models.CharField(max_length=50)
    empaddress=models.CharField(max_length=200)
    empphone=models.CharField(max_length=10)
    empposition=models.CharField(max_length=50,choices=(('SDE I','SDE I'),('SDE II','SDE II'),('SDE III','SDE III')))
    empcompany=models.ForeignKey(Company,on_delete=models.CASCADE)