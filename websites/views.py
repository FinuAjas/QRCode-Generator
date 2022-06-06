from django.shortcuts import render
from . models import Website
from . forms import WebsiteAddForm

def home(request):
    websites = Website.objects.all()
    form = WebsiteAddForm()
    context = {
        'websites': websites,
        'form':form,
    }

    if request.method == 'POST':
        form = WebsiteAddForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html',context)
        else:
            return render(request,'home.html',context)
    else:
        return render(request,'home.html',context)