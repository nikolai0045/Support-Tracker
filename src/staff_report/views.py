from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.models import User
from .models import Staff, PledgeGift, OneTimeGift, Pledge
import csv
import urllib2

class ReportsView(View):
    
    template = 'staff_report/create_reports.html'

    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated():
            return render(request,self.template)
        else:
            return redirect('/home/')


def generate_reports(request):
    url = 'https://colex.littlegreenlight.com/rptlink/c5480763-9e90-4273-8de7-be5a15b8edde'
    response = urllib2.urlopen(url)
    reader = csv.reader(response)
    staff = Staff.objects.all()
    for s in staff:
        for row in reader:
            if row[8] == s.lgl_name:
                if row[6] == "Gift":
                    new_gift = OneTimeGift(
                        
                    )
                elif row[6] == "Pledge":
                    pass
