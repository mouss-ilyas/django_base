# Create your views here.
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import MyModel
from .forms import MyModelForm

def create_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = MyModelForm()
    return render(request, 'myapp/create.html', {'form': form})

def list_view(request):
    items = MyModel.objects.all()
    return render(request, 'myapp/list.html', {'items': items})

def update_view(request, pk):
    item = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        form = MyModelForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('list_view')
    else:
        form = MyModelForm(instance=item)
    return render(request, 'myapp/update.html', {'form': form})

def delete_view(request, pk):
    item = get_object_or_404(MyModel, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('list_view')
    return render(request, 'myapp/delete.html', {'item': item})
