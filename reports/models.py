from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Reports(models.Model):

  ticket              = models.CharField(max_length=255)
  subject             = models.CharField(max_length=255, null=True, blank=True)
  status              = models.CharField(max_length=255, null=True, blank=True)
  agent               = models.CharField(max_length=255, null=True, blank=True)
  group               = models.CharField(max_length=255, null=True, blank=True)
  created_time        = models.CharField(max_length=255, null=True, blank=True)
  closed_time         = models.CharField(max_length=255, null=True, blank=True)
  time_tracked        = models.CharField(max_length=255, null=True, blank=True)
  first_response_time = models.CharField(max_length=255, null=True, blank=True)
  resolution_status   = models.CharField(max_length=255, null=True, blank=True)
  tags                = models.CharField(max_length=255, null=True, blank=True)
  branch              = models.CharField(max_length=255, null=True, blank=True)
  branch_number       = models.CharField(max_length=255, null=True, blank=True)
  field_tech          = models.CharField(max_length=255, null=True, blank=True)
  call_type           = models.CharField(max_length=255, null=True, blank=True)
  printer_serial      = models.CharField(max_length=255, null=True, blank=True)
  km                  = models.CharField(max_length=255, null=True, blank=True)
  travel_time         = models.CharField(max_length=255, null=True, blank=True)
  job_card            = models.CharField(max_length=255, null=True, blank=True)
  dell_call_number    = models.CharField(max_length=255, null=True, blank=True)
  customer_call_ref   = models.CharField(max_length=255, null=True, blank=True)
  area                = models.CharField(max_length=255, null=True, blank=True)
  parts_used          = models.TextField(max_length=255, null=True, blank=True)
  closing_details     = models.CharField(max_length=255, null=True, blank=True)
  users               = models.CharField(max_length=255, null=True, blank=True)
  contactid           = models.CharField(max_length=255, null=True, blank=True)
  company             = models.CharField(max_length=255, null=True, blank=True)
  

  def __str__(self):
      return self.ticket