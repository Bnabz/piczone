from django.shortcuts import render
from django.http  import HttpResponse

def index(request):
    images = Image.objects.all()
    return render(request, 'index.html',{"images":images})
