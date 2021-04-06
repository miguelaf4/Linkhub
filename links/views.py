from django.shortcuts import render
from .models import Link

# Create your views here.
def links(request):
    links = Link.objects.all()
    return render(request, "links/hub.html", {'links': links})