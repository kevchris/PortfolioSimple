from django.shortcuts import render
from .models import job
# Create your views here.
 home(request):
    jobs=Job.objects
    return render(request,'jobs/home.html',{'jobs': jobs})
