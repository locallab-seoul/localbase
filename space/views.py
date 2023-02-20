from django.shortcuts import render
from .models import Spaces

# Create your views here.
def index(request):
    all_spaces = Spaces.objects.all().order_by('-id')
    return render(request, 'index.html', {
        'spaces': all_spaces,
    })