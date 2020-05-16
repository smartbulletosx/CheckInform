from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .analyze import scan
from .forms import DocumentForm

def index(request):
    if request.method == 'POST':
       file = request.FILES['myfile']
       print(file)
       fs = FileSystemStorage()
       filename = fs.save(file.name, file)
       file = fs.url(filename)
       return render(request, 'index.html', {'res': scan(file)})
    return render(request, 'index.html')