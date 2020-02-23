from django.shortcuts import render
from .models import JobListing, CandidatesProfile



# Create your views here.
def home(request):
    job_listings = JobListing.objects.all()
    candidatesprofile = CandidatesProfile.objects.all()
    return render(request,"jobs_app/index.html", {'candidatesprofile': candidatesprofile})





