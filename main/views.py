from .models import Applicants
from django.shortcuts import render
from django.views.generic import CreateView
from django.views import View
from .forms import ApplicationForm


class HomePageView(View):
    def get(self, request):
        template_name = "home.html"
        
        form = ApplicationForm()
        
        return render(request, template_name, {"form": form})
    

class ApplyView(CreateView):
    model = Applicants
    form = ApplicationForm