from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return HttpResponse(request, 'women/index.html')

def about(request):
    return HttpResponse(request, 'women/about.html')

def categories(request, catid):
    if (request.GET):
        print(request.GET)
    return HttpResponse(f"<h1>Category  {catid}</h1>")

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)
    
    return HttpResponse(f"<h1>Archive by year {year}</h1>")

def pageNotFound(request, exception):
    return HttpResponseNotFound("Page not found ")