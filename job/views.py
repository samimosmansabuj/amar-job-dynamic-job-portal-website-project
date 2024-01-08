from django.shortcuts import render

# Create your views here.
def all_job(request):
    return render(request, 'job/job.html')


def job_details(request):
    return render(request, 'job/job_details.html')
