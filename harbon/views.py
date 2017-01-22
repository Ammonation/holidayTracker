from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import htEmployee, holidayRequest
from django.core.urlresolvers import reverse_lazy
## from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
##from .forms import UserForm
from django.views.generic import View

class indexView(generic.ListView):
    template_name="harbon/index.html"
    context_object_name = "allHolidays"

    def get_queryset(self):
        return holidayRequest.objects.all()

class EmployeeView(generic.ListView):
    template_name="harbon/index.html"
    context_object_name = "allEmployees"

    def get_queryset(self):
        return htEmployee.objects.all()

class employeeCreate(CreateView):
    model = htEmployee
    fields = ['firstName','lastName','department','department','mgrUID','mgrFirstName','mgrLastName','holidayAllocation','additonalHoliday']

class holidayRequestCreate(CreateView):
    model = holidayRequest
    fields = ['UID', 'startDate', 'endDate', 'approved']

class holidayRequestApprove(UpdateView):
    model = holidayRequest
    fields=['UID','startDate','endDate','approved']
    template_name_suffix="_update_approve"

class holidayRequestReject(UpdateView):
    model = holidayRequest
    fields=['UID','startDate','endDate','approved']
    template_name_suffix="_update_reject"

class holidayRequestDelete(DeleteView):
    model = holidayRequest
    success_url = reverse_lazy("harbon:index")
