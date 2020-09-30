from django.shortcuts import render
from data_collection.services.populator import Populator


# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST
        url = data.get('url')
        Populator(url).populate()

    return render(request, 'index.html', {})