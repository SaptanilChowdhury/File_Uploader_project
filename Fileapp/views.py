from django.shortcuts import render
from .forms import FileForm
from .models import File

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = FileForm()
    file = File.objects.all()
    return render(request, 'Fileapp/home.html',{'file':file,'form':form})
