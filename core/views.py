from django.shortcuts import render
from .models import Good

# Create your views here.
def homepage(request):
    goods = Good.objects.all()
    return render(request, 'index.html', {'goods': goods})