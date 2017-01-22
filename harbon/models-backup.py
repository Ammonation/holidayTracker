from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

class holidayRequest(models.Model):
    UID = models.CharField(max_length=6)
    startDate = models.DateField(max_length=6)
    endDate = models.DateField(max_length=6)
    approved = models.NullBooleanField(False)

    def get_absolute_url(self):
        return reverse("harbon:index")

class htEmployee(models.Model):
    UID = models.IntegerField(max_length=7, primary_key=True)
    firstName = models.CharField(max_length=25)
    lastName = models.CharField(max_length=25)
    department = models.CharField(max_length=100)

##    department = models.CharField(max_length=100)
##    location = models.CharField(max_length=100)
    mgrUID = models.CharField(max_length=7)
    mgrFirstName = models.CharField(max_length=25)
    mgrLastName = models.CharField(max_length=25)

    holidayAllocation = models.IntegerField()
    additonalHoliday = models.IntegerField()
##    employeeProfilePic = models.FileField()

    def get_absolute_url(self):
        return reverse("harbon:detail", kwargs={"pk":self.pk})

    def get_absolute_url(self):
        return reverse("harbon:index")
