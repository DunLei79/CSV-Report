from django.shortcuts import render, redirect
from .forms import CsvModelForm
from .models import Csv
from reports.models import Reports
import csv

# Create your views here.

def upload_file_view(request):
  form =(CsvModelForm(request.POST or None, request.FILES or None))
  if form.is_valid():
      form.save()
      form=CsvModelForm()
      obj = Csv.objects.get(activated=False)
      with open(obj.file_name.path, encoding="utf8") as f:
        reader = csv.reader(f)
        

        for i, row in enumerate(reader):
          if i == 0:
            pass
          else:

            ticket                = row[0] 
            subject               = row[1] 
            status                = row[2] 
            agent                 = row[3] 
            group                 = row[4] 
            created_time          = row[5] 
            closed_time           = row[6] 
            time_tracked          = row[7] 
            first_response_time   = row[8] 
            resolution_status     = row[9]     
            tags                  = row[10] 
            branch                = row[11] 
            branch_number         = row[12] 
            field_tech            = row[13] 
            call_type             = row[14] 
            printer_serial        = row[15] 
            km                    = row[16] 
            travel_time           = row[17] 
            job_card              = row[18] 
            dell_call_number      = row[19] 
            customer_call_ref     = row[20] 
            area                  = row[21] 
            parts_used            = row[22] 
            closing_details       = row[23] 
            users                 = row[24] 
            contactid             = row[25] 
            company               = row[26] 

            Reports.objects.create(
              ticket                = ticket,
              subject               = subject,        
              status                = status, 
              agent                 = agent, 
              group                 = group,
              created_time          = created_time, 
              closed_time           = closed_time,
              time_tracked          = time_tracked,
              first_response_time   = first_response_time,
              resolution_status     = resolution_status,
              tags                  = tags,
              branch                = branch,
              branch_number         = branch_number,
              field_tech            = field_tech,
              call_type             = call_type,
              printer_serial        = printer_serial,
              km                    = km,
              travel_time           = travel_time,
              job_card              = job_card,
              dell_call_number      = dell_call_number,
              customer_call_ref     = customer_call_ref,
              area                  = area,
              parts_used            = parts_used,
              closing_details       = closing_details,
              users                 = users,
              contactid             = contactid,
              company               = company,
            ) 
            
          
        obj.activated = True  
        obj.save()
        return redirect('report')
        
  return render(request, 'loadcsv/upload.html',{'form': form})
  # return redirect(request, 'reports/roport.html')