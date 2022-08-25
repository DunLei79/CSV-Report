from django.shortcuts import render
from django.http import HttpResponse
from .models import Reports

# Create your views here.

def full_report(request):
  report = Reports.objects.all()
  context = {'report': report}
  return render(request,'reports/report.html', context)



def ticket_report(request,pk):
  ticketObj = Reports.objects.get(id=pk)
  return render(request,'reports/ticket_report.html', {'ticket':ticketObj})
      

