from __future__ import unicode_literals

from django.db import models
import datetime


# Create your models here.
INTERVAL_OPTIONS = {
    'Yearly':1,
    'Semiannually':2,
    'Quarterly':4,
    'Monthly':12,
    'Biweekly':26,
    'Weekly':52,
}

class Staff(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    lgl_name = models.CharField(max_length=40)

class PledgeGift(models.Model):
    amount = models.IntegerField()
    date = models.DateField()

class OneTimeGift(models.Model):
    amount = models.IntegerField()
    date = models.DateField()
    sort_name = models.CharField(max_length=50)
    staff = models.ForeignKey(Staff)

class Pledge(models.Model):
    sort_name = models.CharField(max_length=50)
    staff = models.ForeignKey(Staff)
    pledge_amount = models.IntegerField()
    pledge_balance = models.IntegerField(default=0)
    gifts_per_year = models.IntegerField(choices=INTERVAL_OPTIONS)
    gifts_this_year = models.IntegerField(default=0)
    
    def record_gift(self,gift):
        gift.pledge = self
        gift.save()
        pledge_amount = self.pledge_amount
        for gift in self.pledgegift_set.filter(date__year=datetime.datetime.now().year):
            pledge_amount = pledge_amount - gift.amount
        self.pledge_balance = pledge_amount
        self.save()

class StaffReport(models.Model):
    staff = models.ForeignKey(Staff)
    pledges = models.ManyToManyField(Pledge)
    one_time_gifts = models.ManyToManyField(OneTimeGift)
    date = models.DateField()
