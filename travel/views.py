from django.shortcuts import render

# Create your views here.
def homePageView(request):
    return render(request, 'home.html')

def projectPageView(request):
    return render(request, 'project.html')