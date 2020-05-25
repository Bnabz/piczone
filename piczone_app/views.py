from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image, Location, Category

def index(request):
    images = Image.objects.all()
    return render(request, 'index.html',{"images":images})

def location_filter(request, location):
    images = Image.filter_by_location(location)
    return render(request, 'location.html', {'images': images})

def category_filter(request, category):
    images = Image.search_image_by_category(category)
    return render(request, 'category.html', {'images': images})

def search_results(request):
    if 'searched_image' in request.GET and request.GET["searched_image"]:
        category = request.GET.get("searched_image")
        images = Image.search_image_by_category(category)
        message = f"{category}"
        return render(request, 'search.html', {"message": message, "images": images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {"message": message})
    
